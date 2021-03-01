from rest_framework.decorators import api_view
from utils.security.auth_users import *

# Create your views here.
@api_view(['POST'])
def sysCreation(request):
    data = request.data
    response = create_sys_account(request.FILES['userImage'], data['fullName'], data['password'])
    return response

@api_view(['POST'])
def sysAuthentication(request):
    data = request.data
    response = authenticate_sys_admin(data['userId'], data['password'])
    return response
