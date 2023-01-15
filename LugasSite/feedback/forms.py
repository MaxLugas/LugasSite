from .models import Feedback
from django.forms import ModelForm, TextInput, EmailInput, Textarea, DateInput

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'content', 'date']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your email'
            }),
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your feedback'
            }),
            'date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date'
            }),
        }