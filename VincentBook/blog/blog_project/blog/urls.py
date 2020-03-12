from django.urls import path

from .views import BlogListView, BlogDetailView


app_name = 'blog'
urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
]
