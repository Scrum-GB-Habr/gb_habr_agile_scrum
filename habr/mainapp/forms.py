from django import forms

from authapp.models import AuthorizedUser
from .models import Post, Contact


# class PostForm(forms.ModelForm):
#
#     class Meta:
#         model = Post
#         # fields = "__all__"
#         fields = ('title', 'description',)
#         widgets = {
#             # 'user': forms.HiddenInput(),
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'description': forms.Textarea(attrs={'class': 'form-control'}),
#         }


# не смог разобраться, как запихать в верхнюю форму категорию красиво,
# поэтому переделал
class PostForm(forms.ModelForm):
    """Форма создания статьи"""

    class Meta:
        model = Post
        fields = ('title', 'description', 'category')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


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
