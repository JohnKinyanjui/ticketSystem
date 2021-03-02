from ticket.models import *
from accounts.models import UserModel
from django.http import JsonResponse
from utils.security.generators import generate_ticket_id

def create_ticket(userToken, ticket_type, priority, latitude, longitude, name_of_location):
    if UserModel.objects.filter(token=userToken, role="Ticket Manager") is False:
        return JsonResponse({
            'code':1,
            'message':'Permission Denied'
        })
        
    ticket_types = ["Network Failure", "Survey request", "Material Request"]
    if ticket_type not in ticket_types:
        return JsonResponse({
            'code':1,
            'message': 'This type of ticket is not available'
        })
        
    ticketId = generate_ticket_id()
    new_ticket = TicketModel(
          ticketId = ticketId,
          ticketype = ticket_type, 
          priority = priority,
          latitude = latitude,
          longitude = longitude,
          name_of_location = name_of_location,
    )
    new_ticket.save()
    return JsonResponse({
        'code':0,
        'message':'Ticket created successfully'
    })

def get_tickets(userToken, query):
    if UserModel.objects.filter(token=userToken, role="Field Manager") is False or UserModel.objects.filter(token=userToken, role="Ticket Manager") is False:
        return JsonResponse({
            'code':1,
            'message':'Permission Denied'
        })
    
    ticket = ""
    
    if query == "assigned":
        ticket = TicketModel.objects.filter(assigned=True).all().values()
    elif query == "unassigned":
        ticket = TicketModel.objects.filter(assigned=False).all().values()
    elif query == "overdie":
        ticket = TicketModel.objects.filter(assigned=False).all().values() 
    elif query == "unapproved":
        ticket = TicketModel.objects.filter(approved=False).all().values()           
        
    
        
        
def assign_ticket():
    pass