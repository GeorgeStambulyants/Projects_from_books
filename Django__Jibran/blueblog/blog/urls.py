from django.urls import path

from .views import NewBlogView, UpdateBlogView


urlpatterns = [
    path('new/', NewBlogView.as_view(), name='new_blog'),
    path('<int:pk>/update/', UpdateBlogView.as_view(), name='update_blog')
]
