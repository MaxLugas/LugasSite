from .models import Feedback
from django.forms import ModelForm, TextInput, EmailInput, Textarea, DateInput

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'content', 'date']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nickname'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Feedback'
            }),
            'date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date'
            }),
        }