from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'content', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'News name'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anons'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date'
            }),
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Content'
            }),
        }
