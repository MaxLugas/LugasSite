from .models import Articles
from django.forms import ModelForm, TextInput, DateInput, Textarea, FileInput


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'content', 'file']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'News name'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anons'
            }),
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Content'
            }),
            'file': FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'File'
            }),
        }
