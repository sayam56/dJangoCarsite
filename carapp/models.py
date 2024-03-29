from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


# Create your models here.
class CarType(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='cartype_images/', null=True)  # new line

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    FEATURES = [
        ('CC', 'Cruise Control'),
        ('AI', 'Audio Interface'),
        ('A', 'Airbags'),
        ('AC', 'Air Conditioning'),
        ('SH', 'Seat Heating'),
        ('PA', 'ParkAssist'),
        ('PS', 'Power Steering'),
        ('RC', 'Reversing Camera'),
        ('AS', 'Auto Start/Stop')
    ]
    car_type = models.ForeignKey(CarType, related_name='vehicles', on_delete=models.CASCADE)
    car_name = models.CharField(max_length=200)
    car_price = models.DecimalField(max_digits=12, decimal_places=6)
    inventory = models.PositiveIntegerField(default=10)
    instock = models.BooleanField(default=True)
    product_desc = models.TextField(max_length=255, blank=True, default='')
    car_features = models.CharField(max_length=2, choices=FEATURES, default='A')

    def __str__(self):
        return self.car_name


class Buyer(User):
    AREA_CHOICES = [
        ('W', 'Windsor'),
        ('LS', 'LaSalle'),
        ('A', 'Amherstburg'),
        ('L', 'Lakeshore'),
        ('LE', 'Leamington'),
        ('C', 'Chatham'),
        ('T', 'Toronto'),
        ('WA', 'Waterloo')
    ]

    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    area = models.CharField(max_length=2, choices=AREA_CHOICES, default='C')
    interested_in = models.ManyToManyField(CarType)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.username


# OrderVehicle model representing an order for vehicles
class OrderVehicle(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name='ordered_vehicles', on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, related_name='order_buyer', on_delete=models.CASCADE)
    num_ordered = models.PositiveIntegerField()  # Number of vehicles being ordered
    ORDER_STATUS_CHOICES = [
        (0, 'Cancelled'),
        (1, 'Placed'),
        (2, 'Shipped'),
        (3, 'Delivered'),
    ]
    order_status = models.IntegerField(choices=ORDER_STATUS_CHOICES, default=1)  # Status of the order
    last_updated_date = models.DateField(auto_now=True)  # Date when the order was last updated

    def __str__(self):
        return self.buyer.username

    def total_price(self):
        return self.num_ordered * self.vehicle.car_price


class LabGroupMembers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    semester = models.PositiveIntegerField()
    personal_page_link = models.URLField()

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']
