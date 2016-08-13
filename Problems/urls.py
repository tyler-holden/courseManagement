from django.conf.urls import url, include, patterns
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.post_announcements, name='announcements'),
    url(r'^get_old_announcements/', views.get_old_announcements, name='get_old_announcements'),
    url(r'^problemSet/(?P<pk>\d+)/', views.list_problem_set, name='list_problem_set'),
    url(r'^problemSet/question/(?P<pk>\d+)/$', views.question_details, name='question_details'),
    url(r'^problemSet/question/(?P<pk>\d+)/edit', views.edit_question, name='edit_question'),
    url(r'^announcement/new/', views.new_announcement, name='new_announcement'),
    url(r'^announcement/edit/(?P<pk>\d+)', views.edit_announcement, name='edit_announcement'),
    url(r'^add-question/(?P<listpk>\d+)', views.new_question, name='new_question'),
    url(r'^administrative/add-ps/$', views.new_problem_set, name='new_problem_set'),
    url(r'^delete/(?P<objectStr>[a-z]+)/(?P<pk>\d+)', views.delete_item, name='delete_item'),
    url(r'^syllabus/', views.syllabus, name='syllabus'),
    url(r'^edit_syllabus/', views.edit_syllabus, name='edit_syllabus'),
    url(r'^notes/', views.notes, name='notes'),
    url(r'^calendar/', views.calendar, name='calendar'),
    url(r'^administrative/', views.administrative, name='administrative'),
    url(r'^update_status', views.update_status, name='update_status'),
    url(r'^add-user', views.add_user, name='add_user'),
    url(r'^polls/$', views.polls, name='polls'),
    url(r'^polls/new/$', views.new_poll, name='new_poll'),
    url(r'^polls/(?P<pollpk>\d+)/admin/$', views.poll_admin, name='poll_admin'),
    url(r'^change_question_order', views.change_question_order, name='change_question_order'),
    url(r'^polls/(?P<pollpk>\d+)/show_questions/$', views.list_pollquestions, name='list_pollquestions'),
    url(r'^polls/(?P<pollpk>\d+)/add_question/$', views.new_pollquestion, name='new_pollquestion'),
    url(r'^polls/(?P<pollpk>\d+)/add_question/(?P<questionpk>\d+)/$', views.new_pollquestion, name='new_pollquestion'),
    url(r'^polls/(?P<questionpk>\d+)/edit_question/$', views.edit_pollquestion, name='edit_pollquestion'),
    url(r'^make_live/$', views.make_live, name='make_live'),
    url(r'^live_question/$', views.live_question, name='live_question'),
    url(r'^live_poll/$', views.live_poll, name='live_poll'),
    url(r'^query_live/$', views.query_live, name='query_live'),
    url(r'^pdflatex/$', views.pdflatex, name='pdflatex'),
    url(r'^history/(?P<questionpk>\d+)/(?P<poll_num>-?\d+)/$', views.poll_history, name='poll_history'),
    url(r'^who_voted/(?P<questionpk>\d+)/(?P<poll_num>-?\d+)/$', views.who_voted, name='who_voted'),
    url(r'^upload_file/', views.upload_file, name='upload_file'),
    url(r'^dump_polls/', views.dump_polls, name='dump_polls'),
    url(r'^quiz/add_new', views.new_quiz, name='new_quiz'),
    url(r'^quiz/edit/(?P<quizpk>\d+)/$', views.edit_quiz, name='edit_quiz'),
    url(r'^quiz/list', views.quizzes, name='quizzes'),
    url(r'^quiz/start/(?P<quizpk>\d+)/$', views.start_quiz, name='start_quiz'),
    url(r'^quiz/display_question/(?P<sqrpk>\d+)/$', views.display_question, name='display_question'),
    url(r'^quiz/display_question/(?P<sqrpk>\d+)/(?P<submit>\w+)$', views.display_question, name='display_question'),
    url(r'^quiz/admin/(?P<quizpk>\d+)/$', views.quiz_admin, name='quiz_admin'),
    url(r'^quiz/admin/(?P<quizpk>\d+)/edit_question/$', views.edit_quiz_question, name='edit_quiz_question'),
    url(r'^quiz/admin/(?P<quizpk>\d+)/edit_question/(?P<mpk>\d+)/$', views.edit_quiz_question, name='edit_quiz_question'),
    url(r'^quiz/admin/(?P<mpk>\d+)/edit_choices/$', views.edit_choices, name='edit_choices'),
    url(r'^quiz/test/(?P<mpk>\d+)/$', views.test_quiz_question, name='test_quiz_question'),
    url(r'^quiz/details/(?P<sqrpk>\d+)/$', views.quiz_details, name='quiz_details'),
    url(r'^upload_note/$', views.upload_student_note, name='upload_student_note'),
    url(r'^get_note/(?P<filename>.*)$', views.get_note, name='get_note'),
    url(r'^see_notes/$', views.see_notes, name='see_notes'),
    url(r'^search_notes/$', views.search_notes, name='search_notes'),
    url(r'^admin/create_exemption/$', views.create_exemption, name='create_exemption'),
    url(r'^admin/create_category/$', views.create_file_category, name='create_file_category'),
]
