from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(label='name', max_length=100, required=True)
    email = forms.CharField(label='email', max_length=100, required=True, empty_value=True)
    event = forms.IntegerField(label='event')
    comment = forms.CharField(widget=forms.Textarea)
