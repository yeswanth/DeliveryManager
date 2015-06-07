from django.conf.urls import patterns, include, url
from .views import customer_order,manager_dashboard,assign_delivery_boy
urlpatterns = patterns('',
    url('^$',customer_order, name='customer_order'),
    url('^dashboard/$',manager_dashboard, name='manager_dashboard'),
    url('^assign_delivery_boy/(?P<order_id>[0-9]+)/(?P<boy_id>[0-9]+)$',assign_delivery_boy, name='assign_delivery_boy'),
)
