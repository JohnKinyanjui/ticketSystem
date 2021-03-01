from django.db import models

# Create your models here.
account_roles = ["Field Manager", "Field Agent"]
mtn_account_roles = ["System Admin", "Support"]


class UserModel(models.Model):
    userId = models.CharField(max_length=60)
    userImage = models.ImageField(upload_to='userImages')
    fullName = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    role = models.CharField(max_length=60, choices=account_roles, default="Field Agent")
    token = models.CharField(max_length=120, null=True, blank=True)


class MtnAdmin(models.Model):
    userId = models.CharField(max_length=60)
    userImage = models.ImageField(upload_to='userImages')
    fullName = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    role = models.CharField(max_length=60, choices=mtn_account_roles, default="Support")
    token = models.CharField(max_length=120, null=True, blank=True)
