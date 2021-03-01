from utils.accounts.utils import *
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['POST'])
def createAccount(request):
    data = request.data
    response = create_account(data['userToken'], data['userImage'], data['fullName'], data['password'], data['role'])
    return response


@api_view(['POST'])
def authenticateAccount(request):
    data = request.data
    response = authenticate_account(data['userId'], data['password'])
    return response


@api_view(['POST'])
def getFieldAgents(request):
    response = get_field_agents(request.GET['userToken'])
    return response
