import firebase
from django.conf import settings
APP_URL = settings.FIREBASE_URL
ORDERS_URL = APP_URL + '/orders'
NOTIFICATION_URL = APP_URL + '/notifications'
DELIVERYBOY_URL = APP_URL + '/deliveryboy'

def fb_add_data(url,data):
    fb = firebase.Firebase(url)
    return fb.push(data)

def fb_add_notification(message):
    fb_add_data(NOTIFICATION_URL,message)    

def send_order_notification():
    """
    1. If no delivery boys are assigned, suggest assignment of any of the boys
    2. If one of the delivery boys are assigned in the area, and his status is "WAITING"
        suggest assignment of him
    3. If two or more delivery boys are waiting in the same area, calculate the distance 
        between the order area and the centroid of the remaining deliveries(deliverorder) which are incomplete and choose 
        the delivery boy with the least distance to the centroid 
    """
    pass
