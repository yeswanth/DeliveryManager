from django.db import models
import order.utils as utils

ORDER_STATUS = (
    ('INIT','INIT'),
    ('UNASSIGNED','UNASSIGNED'),
    ('ASSIGNED','ASSIGNED'),
    ('COMPLETED','COMPLETED'),
)

DELIVERY_BOY_STATUS = (
    ('IDLE','IDLE'),
    ('ON THE JOB','ON THE JOB'),
    ('WAITING','WAITING'),
)

AREA_CHOICES = (
    ('BTM','BTM'),
    ('KORAMANGALA','KORAMANGALA'),
    ('INDIRA NAGAR','INDIRA NAGAR'),
)

class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)

class Order(BaseModel):
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)
    status = models.CharField(choices=ORDER_STATUS,default='INIT',max_length=20)
    area = models.CharField(max_length=30,choices=AREA_CHOICES)
    def save(self, *args, **kwargs):
        """
            1. Add order information into firebase along with order items
            2. Add a new notification that an order has been placed 
        """
        items = [i.get_json() for i in self.orderitem_set.all()]
        data = {
            'lat':self.lat,
            'lng':self.lng,
            'status':self.status,
            'area':self.area,
            'items':items
        }
        utils.fb_add_data(utils.ORDERS_URL,data)
        super(Order, self).save(*args,**kwargs)


class OrderItem(BaseModel):
    name = models.CharField(max_length=100)
    order_id = models.ForeignKey(Order)
    quantity = models.IntegerField()
    def get_json(self):
        return {
            'name':self.name,
            'quantity':self.quantity
        }

class DeliveryBoy(BaseModel): 
    name = models.CharField(max_length=100)
    status = models.CharField(choices=DELIVERY_BOY_STATUS,default='IDLE',max_length=20)
    def save(self, *args, **kwargs):
        """
            1. Add delivery boy information into firebase   
        """
        super(DeliveryBoy,self).save(*args,**kwargs)

class DeliveryBoyOrder(BaseModel):
    order_id = models.ForeignKey(Order)
    boy_no = models.ForeignKey(DeliveryBoy)
