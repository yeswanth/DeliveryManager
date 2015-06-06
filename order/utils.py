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
