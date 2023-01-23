from .models import Articles
from django.forms import ModelForm, TextInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'content', 'link']

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
            'link': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'File'
            }),
        }
