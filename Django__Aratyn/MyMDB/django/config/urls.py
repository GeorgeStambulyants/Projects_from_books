from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


handler404 = 'django.views.defaults.page_not_found'

# Won't work if settings.DEBUG = False
MEDIA_FILE_PATHS = static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls', namespace='user')),
    path('', include('core.urls', namespace='core')),
] + MEDIA_FILE_PATHS
