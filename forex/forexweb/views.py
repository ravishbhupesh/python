from django.shortcuts import render
from.forms import IndexForm
import requests, json

curr_convert_url = "http://api.fixer.io/latest?symbols="
curr_convert_base_url = "http://api.fixer.io/latest?base="

#Class based views

# Create your views here.
def index(request):
    form = IndexForm()
    return render(request, 'forexweb/index.html', {'form':form})

def convert(request):
    form = IndexForm(request.POST)
    form.is_valid()
    amount = form.cleaned_data['amount']
    from_curr = form.cleaned_data['from_curr']
    to_curr = form.cleaned_data['to_curr']
    result = 0

    new_url = curr_convert_base_url + from_curr

    response = requests.get(new_url)
    json_resp = json.loads(response.text)
    # fetch date of conversion
    date_of_conversion = json_resp['date']
    # fetch all rates against base currency
    json_resp_curr_dict = json_resp['rates']
    # fetch rate for trget currency
    result = json_resp_curr_dict[to_curr] * amount

    return render(request, 'forexweb/index.html', {
        'form' : form,
        'result': result,
        'date': date_of_conversion
    })

