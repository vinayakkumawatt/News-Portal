
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static



from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name = 'home'),
    path("india/", views.india, name = 'india'),
    path("bollywood/", views.bollywood, name = 'bollywood'),
    path("<int:a>/", views.details, name = 'details'),
    path("search/", views.search, name = 'search'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
