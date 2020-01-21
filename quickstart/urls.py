from django.conf.urls import url

from .views import *
from . import views

urlpatterns = [
    url(r'^signup', CreateUser.as_view()),
    url(r'^login', UserLogin.as_view()),
    url(r'^logout', Logout.as_view()),

    url(r'^get-all-users', GetAllUser.as_view()),
   # url(r'^list-users', ListUser.as_view()),
    url(r'^connect/(?P<pk>\d+)',update_profile.as_view()),
 #   url(r'^friend', friend_list.as_view()),
    url(r'^request', Friend_Request.as_view()),
   # url(r'^update/(?P<pk>\d+)',friend_update.as_view()),
    url(r'^(?P<pk>\d+)', request_detail.as_view()),
    url(r'^friend_list',personal_friend.as_view()),
    url(r'^mixup', List.as_view()),






  #  url('detail/<int:id>/',friend_update.as_view())
 #   url(r'^(?P<pk>\d+)',friend_update.as_view()),

]
