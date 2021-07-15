from django import forms

from authapp.models import AuthorizedUser
from .models import Post, Contact


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = "__all__"
        # fields = ('title', 'description',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'}),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control'}),
            'message_description': forms.Textarea(
                attrs={
                    'class': 'form-control'}),
        }
