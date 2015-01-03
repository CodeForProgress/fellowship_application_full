from django.conf.urls import patterns, url, include
from app import views


urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^forgot_password/$', views.forgot_password, name='forgot_password'),
    url(r'^reset_password/(?P<user_id>\d+)/$', views.reset_password, name='reset_password'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^index/$', views.index, name='index'),
    url(r'^createaccount/$', views.createaccount, name='createaccount'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^background/$', views.background, name='background'),
    url(r'^tech/$', views.tech, name='tech'),
    url(r'^shortanswers/$', views.shortanswers, name='shortanswers'),
    url(r'^recommenders/$', views.recommenders, name='recommenders'),
    url(r'^finalsubmission/$', views.finalsubmission, name='finalsubmission'),
    url(r'^received/$', views.received, name='received'),
    url(r'^my_recommenders/$', views.my_recommenders, name='my_recommenders'),
    url(r'^rec_index/$', views.rec_index, name='rec_index'),
    url(r'^recommend/$', views.my_recommend, name='recommend'),
    url(r'^eval_index/$', views.eval_index, name='eval_index'),
    url(r'^evaluate/(?P<evaluation_id>\d+)/$', views.evaluate, name='evaluate'),
    url(r'^staff_index_applicants/$', views.staff_index_applicants, name='staff_index_applicants'),
    url(r'^staff_index_evaluators/$', views.staff_index_evaluators, name='staff_index_evaluators'),
    url(r'^staff_index_recommenders/$', views.staff_index_recommenders, name='staff_index_recommenders'),
    url(r'^staff_index_staff/$', views.staff_index_staff, name='staff_index_staff'),
    url(r'^assign_evaluator/(?P<applicant_id>\d+)/$', views.assign_evaluator, name='assign_evaluator'),
)