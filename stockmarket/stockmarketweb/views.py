from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView
from .forms import StockQuoteForm
from googlefinance import getQuotes

import requests
import json

base_url = "http://finance.google.com/finance/info?client=ig&q=NASDAQ:"

# Create your views here.

#Class Based Views
class WhoAreWe(TemplateView):
    template_name = "stockmarketweb/whoarewe.html"


#Normal Views
@require_http_methods(["GET"])
def index(request):
    return render(request, 'stockmarketweb/index.html')

@require_http_methods(["GET"])
def bsemain(request):
    form = StockQuoteForm()
    return render(request, 'stockmarketweb/bsemain.html', {'form':form})

@require_http_methods(["POST"])
def getQuote(request):
    form = StockQuoteForm(request.POST)

    symbol = form.cleaned_data['stock_symbol']

    #print(json.dumps(getQuotes(form.cleaned_data['stock_symbol']), indent=2))
    getQuotes(symbol)
    json.d

    return render(request, 'stockmarketweb/stockquote.html')


