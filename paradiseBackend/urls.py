
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('api/', include('apiApp.urls'), name="apiApp-urls"),
    path('apiAdmin/', include('apiAuth.urls'), name="apiAuth-urls")
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
