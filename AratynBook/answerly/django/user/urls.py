from django.urls import path
from django.contib.auth import LoginView, LogoutView
import user.views


app_name = 'user'
urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]
