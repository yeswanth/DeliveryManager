from django.contrib.gis.db import models
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

DELIVERY_BOY_ORDER_STATUS_CHOICES = (
    ('INCOMPLETE','INCOMPLETE'),
    ('COMPLETED','COMPLETED'),
)

class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)

class Order(BaseModel):
    latlng = models.PointField()    
    status = models.CharField(choices=ORDER_STATUS,default='INIT',max_length=20)
    area = models.CharField(max_length=30,choices=AREA_CHOICES)
    fb_key = models.CharField(max_length=30,null=True,blank=True)
    objects = models.GeoManager()
    
    def save(self, *args, **kwargs):
        """
            1. Add order information into firebase along with order items
            2. Add a new notification that an order has been placed 
            TODO 3. If firebase entry exists, then update that entry 
        """
        lat = self.latlng.coords[1]
        lng = self.latlng.coords[0]
        #items = [i.get_json() for i in self.orderitem_set.all()]
        data = {
            'id':self.id,
            'lat':lat,
            'lng':lng,    
            'status':self.status,
            'area':self.area,
        }
        self.fb_key = utils.fb_add_data(utils.ORDERS_URL,data)['name']
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
    def save(self, *args, **kwargs):
        data = {'name':self.name,
                'quantity':self.quantity} 
        utils.fb_add_data(utils.ORDERS_URL+'/'+self.order_id.fb_key+'/items', data)
        super(OrderItem,self).save(*args,**kwargs)
    

class DeliveryBoy(BaseModel): 
    name = models.CharField(max_length=100)
    status = models.CharField(choices=DELIVERY_BOY_STATUS,default='IDLE',max_length=20)
    def save(self, *args, **kwargs):
        """
            1. Add delivery boy information into firebase   
        """
        data = {
            'name':self.name,
            'status':self.status
        } 
        utils.fb_add_data(utils.DELIVERYBOY_URL,data)
        super(DeliveryBoy,self).save(*args,**kwargs)

class DeliveryBoyOrder(BaseModel):
    order_id = models.ForeignKey(Order)
    boy_no = models.ForeignKey(DeliveryBoy)
    status = models.CharField(choices=DELIVERY_BOY_ORDER_STATUS_CHOICES,default='INCOMPLETE',max_length=20)
    def save(self, *args, **kwargs):
        """
        1. Add this into firebase
        TODO 
        """
        super(DeliveryBoyOrder,self).save(*args,**kwargs)
