from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . views import UserRegistrationView


urlpatterns = [
    path(
        'new-user/', UserRegistrationView.as_view(), name='user_registration'
    ),
    path(
        'login/', LoginView.as_view(), name='login'
    ),
    path(
        'logout/', LogoutView.as_view(), name='logout'
    )
]
