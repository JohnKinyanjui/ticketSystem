from django.urls import path
from .views import *

urlpatterns = [
    path('createTicket', createTicket),
    path('assignTicket', assignTicket),
    path('getTickets', getTickets),
]