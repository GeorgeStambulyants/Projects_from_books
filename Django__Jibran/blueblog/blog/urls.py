from django.urls import path

from .views import NewBlogView


urlpatterns = [
    path('new/', NewBlogView.as_view(), name='new_blog'),
]
