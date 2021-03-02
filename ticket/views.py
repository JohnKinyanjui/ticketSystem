from utils.ticket.utils import *
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['POST'])
def createTicket(request):
    data = request.data
    response = create_ticket(data['userToken'], data['ticket_type'], data['priority'], data['latitude'], data['longitude'], data['name_of_location'])
    return response