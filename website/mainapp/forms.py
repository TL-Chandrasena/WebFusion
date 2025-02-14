from django import forms
from .models import LogMessage

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ['name','class_field','message',]
        
