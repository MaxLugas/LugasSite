from django.urls import path
from . import views
from .views import RegisterUser

urlpatterns = [
    path('', views.index, name='home'),
    path('contacts', views.contacts, name='contacts'),
    path('about', views.about, name='about'),
    path('login', views.sign_in, name='sign_in'),
    path('register', RegisterUser.as_view(), name='register'),
]
