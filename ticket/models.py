from django.db import models


# Create your models here.
class TicketModel(models.Model):
    ticketId = models.CharField(max_length=60)
    ticketDate = models.DateTimeField()
    ticketInfo = models.CharField(max_length=2000)
    userId = models.CharField(max_length=20, null=True, blank=True)
    assigned = models.BooleanField(default=False)

