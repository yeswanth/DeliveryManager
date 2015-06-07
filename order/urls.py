from django.conf.urls import patterns, include, url
from .views import customer_order
urlpatterns = patterns('',
    url('^$',customer_order, name='customer_order'),
)
