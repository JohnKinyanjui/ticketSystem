from utils.ticket.utils import *
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['POST'])
def createTicket(request):
    data = request.data
    response = create_ticket(
        data['userToken'],
        data['ticket_type'],
        data['deadline'],
        data['priority'],
        data['latitude'], 
        data['longitude'],
        data['name_of_location']
        )
    return response

@api_view(['POST'])
def assignTicket(request):
    data = request.data
    response = assign_ticket(data['userToken'], data['ticketId'], data['userId'])
    return response

@api_view(['GET'])
def getTickets(request):
    response = get_tickets(request.GET['userToken'], request.GET['query'])
    return response

