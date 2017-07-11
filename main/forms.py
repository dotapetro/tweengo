from django import forms


class PostImageForm(forms.Form):
    image = forms.ImageField()
