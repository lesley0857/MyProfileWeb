
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from profileapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
