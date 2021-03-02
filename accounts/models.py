from django.db import models

# Create your models here

class UserModel(models.Model):
    userId = models.CharField(max_length=60)
    userImage = models.ImageField(upload_to='userImages')
    fullName = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    role = models.CharField(max_length=60, default="Field Agent")
    token = models.CharField(max_length=120, null=True, blank=True)
