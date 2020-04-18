from django.urls import path

from .views import send_login_mail


urlpatterns = [
    path(
        'send_login_mail', send_login_mail, name='send_login_mail'
    )
]
