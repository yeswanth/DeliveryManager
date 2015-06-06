from django.shortcuts import render

def assign_delivery_boy(request,order_id,boy_id):
    """
    1. Add entry DeliveryBoyOrder 
    TODO 
    """
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
    pass

def manager_dashboard(request):
    """
    This view will be shown to the manager 
    """
    pass
