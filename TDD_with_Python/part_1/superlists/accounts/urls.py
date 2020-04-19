from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import send_login_mail, login


urlpatterns = [
    path(
        'send_login_mail', send_login_mail, name='send_login_mail',
    ),
    path(
        'login', login, name='login',
    ),
    path(
        'logout', LogoutView.as_view(), name='logout'
    ),
]
