from django.urls import path
from .views import *
urlpatterns =[
    path('createAccount', createAccount),
    path('authenticateAccount', authenticateAccount),
    path('getFieldAgents', getFieldAgents),
]
