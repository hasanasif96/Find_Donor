from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

Blood_choices = (
    ("Don't know", "Don't know"),
    ("O+", "O+"),
    ("O-", "O-"),
    ("A+", "A+"),
    ("A-", "A-"),
    ("B+", "B+"),
    ("B-", "B-"),
    ("AB+", "AB+"),
    ("AB-", "AB-"),
)

class Donor(models.Model):
    d_user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    age=models.CharField(max_length=4)
    Blood_Group = models.CharField(max_length=50, choices=Blood_choices)
    city = models.CharField(max_length=20)
    when_Recovered= models.DateTimeField()
    description = models.CharField(max_length=80)
    

    def __str__(self):
        return self.slug
    
    
    
ORDER_STATUS = (
    ("Request Received", "Request Received"),
    ("Request Pending", "Request Processing"),
    ("Request Accepted", "Request Accepted"),
    ("Request Cancelled", "Request Cancelled"),
)

situation_choices = (
    ("Very Serious", "Very Serious"),
    ("In Ventilator", "In Ventilator"),
    ("Oxygen Below 50", "Oxygen Below 50"),
    ("Not so serious", "Not so serious"),

)

class requests(models.Model):
    name=models.CharField(max_length=20)
    create_by= models.ForeignKey(Customer, on_delete=models.CASCADE)
    donor= models.ForeignKey(Donor, on_delete=models.CASCADE)
    city = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    currrent_situation = models.CharField(max_length=40, choices=situation_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS, default="Request Pending")
    

    def __str__(self):
        return "Request: " + str(self.id)
