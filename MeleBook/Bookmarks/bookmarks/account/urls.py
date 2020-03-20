from django.urls import path
from django.contrib.auth import views as auth_views

from .import views as account_views


urlpatterns = [
    # path(
    #     'login/',
    #     account_views.user_login,
    #     name='http://127.0.0.1:8000/account/login/login',
    # ),
    path(
        'login/',
        auth_views.LoginView.as_view(),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout',
    ),
    path(
        '', 
        account_views.dashboard,
        name='dashboard'
    ),
]