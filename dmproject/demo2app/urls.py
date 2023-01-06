from django.conf.urls.static import static

from dmproject import settings
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),


]