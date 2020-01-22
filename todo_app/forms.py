from django import forms
from django.forms import ModelForm
from todo_app.models import item


class itemForm(ModelForm):
    """Form definition for item."""
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholer': 'Title',
        }))

    class Meta:

        model = item
        fields = "__all__"

    # def __init__(self, *args, **kwargs):
    #     # first call parent's constructor
    #     super(itemForm, self).__init__(*args, **kwargs)
    #     # there's a `fields` property now
    #     self.fields['title'].required = False
