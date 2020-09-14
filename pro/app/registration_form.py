from django import forms
from app.models import user_registration,todolist_info

class registration_form(forms.ModelForm):
    user_password=forms.CharField(widget=forms.PasswordInput,max_length=30)
    class Meta:
        model=user_registration
        fields='__all__'

class todolist_form(forms.ModelForm):
    class Meta:
        model=todolist_info
        fields=('event_name','event_description')
