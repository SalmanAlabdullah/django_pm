from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _
from . import models

attrs = {'class':'form-control'}

class ProjectCreateForm(forms.ModelForm):
    class Meta():
        model = models.Project
        fields = ['category','title','description']
        labels = {
            'category': _('Category'),
            'title': _('Title'),
            'description': _('Description')
        }
        widgets = {
            'category': forms.Select(attrs=attrs),
            'title' : forms.TextInput(attrs=attrs),
            'description' : forms.Textarea(attrs=attrs)
        }


class ProjectUpdateForm(forms.ModelForm):
    class Meta():
        model = models.Project
        fields = ['category', 'title', 'status']
        widgets = {
            'category': forms.Select(attrs=attrs),
            'title': forms.TextInput(attrs=attrs),
            'status': forms.Select(attrs=attrs)
        }


