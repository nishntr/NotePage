from django import forms
from django.forms import ModelForm
from todo_app.models import item


class itemForm(ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholer': 'Title',
        }))

    class Meta:

        model = item
        fields = "__all__"
