from django.conf.urls import url, include, patterns
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.post_announcements, name='announcements'),
    url(r'^problemSet/(?P<pk>\d+)/', views.list_problem_set, name='list_problem_set'),
    url(r'^question/(?P<pk>\d+)/', views.question_details, name='question_details'),
    url(r'^announcement/new/', views.new_announcement, name='new_announcement'),
    url(r'^announcement/edit/(?P<pk>\d+)', views.edit_announcement, name='edit_announcement'),
    url(r'^add-question/(?P<listpk>\d+)', views.new_question, name='new_question'),
    url(r'^delete/(?P<objectStr>[a-z]+)/(?P<pk>\d+)', views.delete_item, name='delete_item'),
    url(r'^syllabus/', views.syllabus, name='syllabus'),
    url(r'^calendar/', views.calendar, name='calendar'),
    url(r'^administrative/', views.administrative, name='administrative'),
    url(r'^update_status', views.update_status, name='update_status'),
]
