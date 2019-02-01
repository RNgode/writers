# Here we are simply desghning how our database tables will look like
# class names translates to table names while fields become columns.
# functions inside classes give  actions that can be undertakent on these tables

from django.conf import settings
from django.db import models
from django.utils import timezone
# from phonenumber_field.modelfields import phonenumberField


class Status(models.Model):
    is_available = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    is_editing = models.BooleanField(default = False)
    is_paid=models.BooleanField(default=False)
    is_rejected=models.BooleanField(default=False)

# Order's table
class Order(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   # writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    order_topic = models.CharField(max_length=200, blank=True)
    order_description = models.TextField(blank=True)
    track_number = models.IntegerField()
    status=models.ForeignKey(Status, default=1, on_delete=models.CASCADE)
    # is_paid = models.BooleanField(default=False)
    date_created = models.DateTimeField()
    deadline = models.DateTimeField()
    # is_available = models.BooleanField(default=False)
    # is_pending = models.BooleanField(default=False)
    # is_approved = models.BooleanField(default=False)
    # is_editing = models.BooleanField(default = False)
    order_files = models.CharField(max_length=200, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def assignorder(self):
        status= status.is_available(False)
        self.save()


    def __str__(self):
        return self.order_topic

    #comments table: Allows the client to post their satisfaction or dispute on services received.
class Comment(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time=models.DateTimeField()
    is_seen=models.BooleanField(default=False)

    #Bid table: This is the connection between the orders done by the clients and the the writers bidding on the order
class Bid(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bid_amount=models.IntegerField()


     #Client table: Information about the client
class Client(models.Model):
    first_name=models.CharField(max_length=200, blank=True)
    last_name=models.CharField(max_length=200, blank=True)
    email_address=models.CharField(max_length=200, blank=True)
    phonenumber=models.IntegerField(null=False, blank=False, default=0)


    #Administration table
class Admin(models.Model):
    first_name=models.CharField(max_length=200, blank=True)
    last_name=models.CharField(max_length=200, blank=True)
    email_address=models.CharField(max_length=200, blank=True)
    phonenumber=models.IntegerField(null=False, blank=False, default=0)


    #Writers table
class Writer(models.Model):
    first_name=models.CharField(max_length=200, blank=True)
    last_name=models.CharField(max_length=200, blank=True)
    email_address=models.CharField(max_length=200, blank=True)
    phonenumber=models.IntegerField(null=False, blank=False, default=0)

