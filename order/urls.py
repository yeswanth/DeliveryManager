from django.conf.urls import patterns, include, url
from .views import customer_order,manager_dashboard
urlpatterns = patterns('',
    url('^$',customer_order, name='customer_order'),
    url('^dashboard/$',manager_dashboard, name='manager_dashboard'),
)
