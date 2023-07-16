
from django.urls import path
from django.urls.conf import include

from User import apis
from . import views
urlpatterns = [
    path('send_mail/', apis.SendMailToUsersApi.as_view(),
         name='send_mail_to_all_users'),
    path('list/', apis.UserListApi.as_view(), name="users_list")
]
