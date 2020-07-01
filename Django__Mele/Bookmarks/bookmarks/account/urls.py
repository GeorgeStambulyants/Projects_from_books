from django.urls import path, include

from .import views as account_views


urlpatterns = [
    path(
        '', 
        account_views.dashboard,
        name='dashboard'
    ),
    path(
        '',
        include('django.contrib.auth.urls')
    ),
    path(
        'register/',
        account_views.register,
        name='register'
    ),
    path(
        'edit/',
        account_views.edit,
        name='edit'
    ),
    path(
        'users/',
        account_views.user_list,
        name='user_list',
    ),
    path(
        'users/follow/',
        account_views.user_follow,
        name='user_follow',
    ),
    path(
        'users/<username>/',
        account_views.user_detail,
        name='user_detail',
    ),
]
