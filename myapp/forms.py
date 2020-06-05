from django import forms
from django.forms import ModelForm
from . import models

class Studentform(forms.ModelForm):
    class Meta:
        model = models.Students
        fields = '__all__'