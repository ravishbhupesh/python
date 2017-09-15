from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),

    #url(r'^convert$', views.convert, name='convert'),
    #url(r'^$', TemplateView.as_view(template_name="forexweb/index.html"), name='index'),
    #url(r'^basemain$', views.bsemain, name='bsemain'),
    #url(r'^whoarewe$', views.whoarewe, name='whoarewe'),
    #url(r'^whoarewe/$', TemplateView.as_view(template_name="stockmarketweb/whoarewe.html")),
    #url(r'^whoarewe/$', WhoAreWe.as_view(), name='whoarewe'),
    #url(r'^getQuote$', views.getQuote, name="getQuote"),
]