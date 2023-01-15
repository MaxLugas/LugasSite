from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_home, name='feedback_home'),
    path('create_feedback', views.create_feedback, name='create_feedback'),
    path('<int:pk>', views.FeedbackDetailView.as_view(), name='feedback-detail')
]
