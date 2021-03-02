from django.db import models


# Create your models here.
class TicketModel(models.Model):
    ticketId = models.CharField(max_length=60)
    ticketype = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()
    agent = models.CharField(max_length=20, null=True, blank=True)
    priority = models.CharField(max_length=40)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    name_of_location = models.CharField(max_length=300)
    assigned = models.BooleanField(default=False)
    approved = models.BooleanField(null=True, blank=True)
    
class MailModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    mail_message = models.CharField(max_length=30)
    ticket_id = models.CharField(max_length=60)
