from django.db import models
from utils.security.utils import hash_password

class SystemUser(models.Model):
    userId = models.CharField(max_length=60)
    userImage = models.ImageField(upload_to='userImages')
    fullName = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    token = models.CharField(max_length=120, null=True, blank=True)