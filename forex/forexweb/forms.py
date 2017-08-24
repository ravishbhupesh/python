from django import forms

class IndexForm(forms.Form):
    amount = forms.IntegerField(label='Amount ', initial=1)
    from_curr = forms.CharField(label='From ', max_length=5, initial='EUR')
    to_curr = forms.CharField(label='To ', max_length=5, initial='INR')


