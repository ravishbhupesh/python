from django import forms

class StockQuoteForm(forms.Form):
    stock_symbol = forms.CharField(label='Stock Symbol', max_length=50)