from django.conf.urls import url
from django.views.generic import TemplateView

from . import views
from .views import WhoAreWe

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^basemain$', views.bsemain, name='bsemain'),
    #url(r'^whoarewe$', views.whoarewe, name='whoarewe'),
    #url(r'^whoarewe/$', TemplateView.as_view(template_name="stockmarketweb/whoarewe.html")),
    url(r'^whoarewe/$', WhoAreWe.as_view(), name='whoarewe'),
    url(r'^getQuote$', views.getQuote, name="getQuote"),
]