from django.urls import path
from . import views
from .views import RegisterUser, LoginUser, logout_user

urlpatterns = [
    path('', views.index, name='home'),
    path('contacts', views.contacts, name='contacts'),
    path('about', views.about, name='about'),
    path('signin', LoginUser.as_view(), name='sign_in'),
    path('signup', RegisterUser.as_view(), name='register'),
    path('logout', logout_user, name='logout'),
    path('certificates', views.certificates, name='certificates'),
]
