from django.shortcuts import render
from .models import Subscriber
from .forms import SubscriberForm
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            subscriber = Subscriber(sub_name = form.cleaned_data['sub_name'],
                                    sub_email = form.cleaned_data['sub_email'])
            subscriber.save()
            return HttpResponseRedirect('/')
    else:
        form = SubscriberForm()

    return render(request, 'webmod/index.html',{'form':form})