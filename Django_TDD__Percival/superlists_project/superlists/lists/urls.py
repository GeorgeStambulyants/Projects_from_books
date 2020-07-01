from django.urls import path, re_path
from lists import views


urlpatterns = [
    path('new', views.new_list, name='new_list'),
    path('<int:id>/', views.view_list, name='view_list'),
    re_path(r'users/(.+)/', views.my_lists, name='my_lists')
]
