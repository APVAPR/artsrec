from django import forms
from .models import *


class AddPostForm(forms.Form):
    title_post = forms.CharField(max_length=255, label='Название')
    slug = forms.SlugField(max_length=255, label='URL')
    image = forms.ImageField()
