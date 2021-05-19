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



class Donor(models.Model):
    d_user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)
    city = models.CharField(max_length=20)
    when_Recovered= models.DateTimeField()
    description = models.CharField(max_length=40)
    

    def __str__(self):
        return self.slug
    
    
    
ORDER_STATUS = (
    ("Request Received", "Request Received"),
    ("Request Pending", "Request Processing"),
    ("Request Accepted", "Request Accepted"),
    ("Request Cancelled", "Request Cancelled"),
)



class requests(models.Model):
    name=models.CharField(max_length=20)
    create_by= models.ForeignKey(Customer, on_delete=models.CASCADE)
    donor= models.ForeignKey(Donor, on_delete=models.CASCADE)
    city = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    currrent_situation = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS, default="Request Pending")
    

    def __str__(self):
        return "Request: " + str(self.id)