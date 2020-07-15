from django.contrib import admin
from django.urls import path, include

from blog.views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('blog.urls')),
    path('', HomeView.as_view(), name='home'),
]
