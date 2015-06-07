from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse
from .models import DeliveryBoyOrder,DeliveryBoy,Order

def assign_delivery_boy(request,order_id,boy_id):
    """
    1. Add entry DeliveryBoyOrder 
    2. Update 
    """
    order = Order.objects.get(pk=order_id)
    order.status = 'ASSIGNED'
    order.save()
    boy = DeliveryBoy.objects.get(pk=boy_id) 
    boy.status = 'WAITING'
    boy.save()
    dbo = DeliveryBoyOrder(order_id=order,boy_no=boy)
    dbo.save() 
    return HttpResponse('Success')

def update_delivery_boy_status(request,boy_id,status):
    """
    1. Update delivery boy status
    2 If status is completed, save delivery boy status as 'Idle' 
        and delivery boy order status as 'completed' 
        and order status as 'completed'
    """
    return HttpResponse('Success')

def update_order_status(request,order_id,status):
    """
    1. update order status
    """
    return HttpResponse('Success')

def customer_order(request):
    """
    This view will be shown to the customer who is ordering from the site
    1. Get -> get order 
    2. Post -> 
        i. save order
        ii. send notification 
    """
    return render_to_response('customer_order.html')

def manager_dashboard(request):
    """
    This view will be shown to the manager 
    """
    return render_to_response('index.html')
