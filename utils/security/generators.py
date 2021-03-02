import jwt
from django.conf import settings
from datetime import date, datetime, timedelta
from accounts.models import *
import random
import string
from ticket.models import TicketModel


def _generate_jwt_token():
    dt = datetime.now() + timedelta(days=60)
    token = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(50))
    return token


def token_generator():
    result = _generate_jwt_token
    token_exists = UserModel.objects.filter(token=result).exists()
    while token_exists is True:
        result = _generate_jwt_token
    else:
        return _generate_jwt_token()

def generate_account_id(type):
    todays_date = date.today()
    if type == "Field Agent":
        no = UserModel.objects.all().count() + 1
        id = "FAG" + str(no) + "/" + str(todays_date.year)
        while UserModel.objects.filter(userId=id).exists():
            no = UserModel.objects.all().count() + 1
            id = "FAG" + str(no) + "/" + str(todays_date.year)
            continue
        else:
            return id
    elif type == "Field Manager": 
          no = UserModel.objects.all().count() + 1
          id = "FMN" + str(no) + "/" + str(todays_date.year)
          while UserModel.objects.filter(userId=id).exists():
            no = UserModel.objects.all().count() + 1
            id = "FMN" + str(no) + "/" + str(todays_date.year)
            continue
          else:
            return id  
    
def generate_ticket_id():
    todays_date = date.today()
    no = TicketModel.objects.all().count() + 1
    id = "TK" + str(no) + "/" + str(todays_date.year)
    while TicketModel.objects.filter(userId=id).exists():
        no = TicketModel.objects.all().count() + 1
        id = "TK" + str(no) + "/" + str(todays_date.year)
        continue
    else:
        return id            