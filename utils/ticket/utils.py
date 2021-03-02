from ticket.models import *
from accounts.models import UserModel
from django.http import JsonResponse
from utils.security.generators import generate_ticket_id

def create_ticket(userToken, ticket_type, deadline, priority, latitude, longitude, name_of_location):
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
          deadline = deadline,
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
    elif query == "overdue":
        ticket = TicketModel.objects.filter(assigned=False).all().values() 
    elif query == "unapproved":
        ticket = TicketModel.objects.filter(approved=False).all().values()     
    elif query == "approved":  
        ticket = TicketModel.objects.filter(approved=True).all().values()     
        
    return JsonResponse({
        'code':0,
        'tickets': list(ticket)
    })            
        
    
        
        
def assign_ticket(userToken, ticketId, userId):
    if UserModel.objects.filter(token=userToken, role="Field Manager") is False or UserModel.objects.filter(token=userToken, role="Ticket Manager") is False:
        return JsonResponse({
            'code':1,
            'message':'Permission Denied'
        })
    
    if UserModel.objects.filter(userId=userId).exists() is False:
        return JsonResponse({
            'code':1,
            'message':'This field agent does not exists'
        })
        
    if TicketModel.objects.filter(ticketId=ticketId).exists() is False:
        return JsonResponse({
            'code':1,
            'message':'This ticket does not exists'
        })
    
    TicketModel.objects.filter(ticketId=ticketId).update(userId=userId, assigned=True)
    
    return JsonResponse({
        'code':0,
        'message':'Ticket updated'
    })
        
    