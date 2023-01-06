from django.conf.urls.static import static

from dmproject import settings
from . import views, admin
from django.urls import path

urlpatterns = [

    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
]
