from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views
from .views import TaskList, TaskDetail, UserList, UserDetail

urlpatterns = [
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^tasks/$', TaskList.as_view()),
    url(r'^tasks/(?P<pk>[0-9]+)$', TaskDetail.as_view()),
    url(r'^users/$', UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
