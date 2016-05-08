from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.views import password_change
from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail

import json

from django.contrib.auth.models import User
from .models import Announcement, ProblemSet, Question, QuestionStatus, Poll, PollQuestion, PollChoice
from .forms import AnnouncementForm, QuestionForm, ProblemSetForm, NewStudentUserForm, PollForm

# Create your views here.

def staff_required(login_url='/accounts/login/'):
    return user_passes_test(lambda u:u.is_staff, login_url=login_url)

# @login_required
def post_announcements(request):
    posts = Announcement.objects.filter(expires__gte=timezone.now()).order_by('-stickied', '-published_date')
    return render(request, 'Problems/post_announcements.html', {'announcements': posts})

def get_old_announcements(request):
    posts = Announcement.objects.filter(expires__lte=timezone.now()).order_by('-stickied', '-published_date')
    return render(request, 'Problems/old_announcements.html', {'ann': posts})

@staff_required()
def new_announcement(request):
    if request.method == "POST":
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish()
            return redirect(post_announcements)
    else:
        form = AnnouncementForm()

    return render(request, 'Problems/edit_announcement.html', {'form' : form})

@staff_required()
def edit_announcement(request, pk):
    post = get_object_or_404(Announcement, pk=pk)
    if request.method == "POST":
        form = AnnouncementForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish()
            return redirect(post_announcements)
    else:
        form = AnnouncementForm(instance=post)

    return render(request, 'Problems/edit_announcement.html', {'form' : form})
#
# Deletes either an item or a list, as given by the string object_type
# Checks to see if the user is allowed access
@staff_required()
def delete_item(request, objectStr, pk):
    if request.user.is_staff:
        # Depending on which item is set, we return different pages
        if objectStr == "announcement":
            theObj      = get_object_or_404(Announcement, pk = pk)
            return_View = redirect('/')
        elif objectStr == "question":
            theObj      = get_object_or_404(Question, pk = pk)
            return_View = redirect('list_problem_set', pk=theObj.problem_set.pk)
        else:
            return HttpResponse('<h1>Invalid Object Type</h1>')

        if request.method == "POST":
            theObj.delete()
            return return_View
        else:
            return render(request, 'Problems/delete_item.html', {'object': theObj, 'type' : objectStr})
    else:
        return HttpResponseForbidden()

@staff_required()
def new_question(request, listpk):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        ps   = get_object_or_404(ProblemSet, pk=listpk)
        if form.is_valid():
            question = form.save(commit=False)
            question.problem_set = ps
            question.save()
            return redirect('list_problem_set', pk=listpk)
    else:
        form = QuestionForm()

    return render(request, 'Problems/edit_announcement.html', {'form' : form})

@staff_required()
def edit_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('list_problem_set', pk=question.problem_set.pk)
    else:
        form = QuestionForm(instance=question)

    return render(request, 'Problems/edit_announcement.html', {'form' : form})

@staff_required()
def new_problem_set(request):
    if request.method == "POST":
        form = ProblemSetForm(request.POST)
        if form.is_valid():
            problem_set= form.save(commit=False)
            problem_set.save()
            return redirect('administrative')
    else:
        form = ProblemSetForm()

    return render(request, 'Problems/edit_announcement.html', {'form' : form})

@staff_required()
def post_delete(request, pk):
    post = get_object_or_404(Announcement, pk=pk)
    post.delete()
    return redirect('post_list')

@login_required
def syllabus(request):
    return render(request, 'Problems/syllabus.html')

@login_required
def calendar(request):
    return render(request, 'Problems/calendar.html')

@login_required
def notes(request):
    return render(request, 'Problems/notes.html')

@staff_required()
def administrative(request):
    if request.user.is_staff:
        return render(request, 'Problems/administrative.html')
    else:
        return HttpResponseForbidden()

@login_required
def list_problem_set(request, pk):
    ps = get_object_or_404(ProblemSet, pk=pk)

    # There is no standary sort_by on the charfield that returns difficulty, so we use the 'extra' method
    #CASE_SQL = '(case when difficulty="E" then 1 when difficulty="M" then 2 when difficulty="H" then 3 when difficulty="I" then 4 end)'
    #problems = ps.problems.extra(select={'difficulty': CASE_SQL}, order_by=['difficulty'])
    problems = ps.problems.order_by('difficulty', 'pk')
    return render(request, 'Problems/list_problem_set.html', {'problems': problems, 'problem_set': ps})

@csrf_protect
@login_required
def question_details(request, pk):
    problem = get_object_or_404(Question, pk=pk)
    problemStatus, created = QuestionStatus.objects.get_or_create(user=request.user, question=problem)

    if request.method == "POST":
        solution = request.POST['solution']
        problemStatus.solution = solution
        problemStatus.save()

    return render(request, 'Problems/question_details.html', {'problem': problem, 'status': problemStatus})

@csrf_protect
@login_required
def update_status(request):
    try:
        user     = get_object_or_404(User, pk=int(request.POST['user']))
        question = get_object_or_404(Question, pk=int(request.POST['question']))
        status   = get_object_or_404(QuestionStatus, user=user, question=question)
    except:
        raise Http404('A variable was not correctly defined');

    response_data = {'response': ''}

    diff_int = int(request.POST['difficulty'])

    if diff_int > 10 or diff_int < 1:
        response_data['response'] = 'Must pass an integer between 1 and 10. Data not saved'
        return HttpResponse(json.dumps(response_data))

    if user == request.user:
        status.attempt    = (request.POST['attempted'].lower() == 'true')
        status.solved     = (request.POST['solved'].lower() == 'true')
        status.difficulty = diff_int
        status.save()
        response_data['response']='Status successfully updated!'
    else:
        raise HttpResponseForbidden()

    return HttpResponse(json.dumps(response_data))

@staff_required()
def add_user(request):
# Create a new user, generate a random password, and email it
    if request.method == 'POST':
        form = NewStudentUserForm(request.POST)
        un = request.POST['username']
        em = request.POST['email']

        user  = User(username=un, email=em)
        rpass = User.objects.make_random_password()
        user.set_password(rpass)
        
        subject = "You have just been added to MAT237!"
        message = """ You have just been added to the MAT237 course website, located at

http://www.utmat237.com

Your username is {username} and your password is {password}. 
Please login and change your password
            """.format(username=un, password=rpass)

        send_mail(subject, message, 'mat237summer2016@gmail.com', [em])
        user.save()

        return redirect('administrative')
    else:
        form = NewStudentUserForm()

    return render(request, 'Problems/edit_announcement.html', {'form' : form})

@login_required
def polls(request):
    polls = Poll.objects.all()

    return render(request, 'Problems/list_polls.html', {'polls' : polls})

@staff_required()
def new_poll(request):
    if request.method == "POST":
        form = PollForm(request.POST)
        if form.is_valid():
            poll = form.save()
            return redirect('polls')
    else:
        form = PollForm()

    return render(request, 'Problems/edit_announcement.html', {'form' : form})

# Only handles rendering the poll admin page. AJAX requests handled by other views
@staff_required()
def poll_admin(request, pollpk):
    poll = get_object_or_404(Poll, pk=pollpk)
    return render(request, 'Problems/poll_admin.html', {'poll': poll})

@staff_required()
def new_question(request, pollpk, questionpk=None):
# To facilitate question + choice at the same time, we must instantiate the
# question before hand. This will also make editing a question easy in the
# future

    poll = get_object_or_404(Poll, pk=pollpk)

    # If a question is created, we must instantiate it
    if questionpk is None:
        question = PollQuestion(poll=poll)

    if request.method == "POST":
        return redirect('poll_admin')

    else:
        return render(request, 'Problems/new_question.html', {'question' : question})
