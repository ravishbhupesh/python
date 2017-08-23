from django.shortcuts import render
from django.http import HttpResponse
from.forms import IndexForm

# Create your views here.
def index(request):
    form = IndexForm()
    return render(request, 'forexweb/index.html', {'form':form})

def convert(request):
    form = IndexForm(request.POST)
    print(form.is_valid())
    print(form.cleaned_data['from_curr'])
    print(form.cleaned_data['to_curr'])

    return HttpResponse("This is yet to be implemented!")

