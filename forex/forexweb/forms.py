from django import forms

class IndexForm(forms.Form):
    from_curr = forms.CharField(label='From ', max_length=10, initial='USD')
    to_curr = forms.CharField(label='To ', max_length=10, initial='INR')