from django.urls import path
from .views import *

urlpatterns = [
    path('sysCreation', sysCreation),
    path('sysAuthentication', sysAuthentication)
]