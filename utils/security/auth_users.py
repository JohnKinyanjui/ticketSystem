from django.contrib.auth.models import User
from django.http import JsonResponse
from security.models import SystemUser
from utils.security.generators import generate_account_id
from utils.security.utils import *
from utils.security.generators import _generate_jwt_token
from django.utils.datetime_safe import date

def create_sys_account(userImage, fullName, password):
    todays_date = date.today()
    userId = "SYS" + fullName[0] + fullName[-1] + "/" + str(todays_date.year)

    userModel = SystemUser(
        userId= userId,
        userImage= userImage,
        fullName= fullName,
        password= hash_password(password),
    )
    userModel.save()
    return JsonResponse({
        'code': 0,
        'userId': userId,
        'message': 'System Account created',
    })

def authenticate_sys_admin(userId, password):
    if SystemUser.objects.filter(userId=userId).exists():
        user = SystemUser.objects.get(userId=userId)
        if check_password(user.password, password):
            result = _generate_jwt_token
            token_exists = SystemUser.objects.filter(token=result).exists()
            while token_exists is True:
                result = _generate_jwt_token
            
            token = _generate_jwt_token()
            SystemUser.objects.filter(userId=userId).update(token=token) 
            return JsonResponse({
                'code':0,
                'token':token,
            })
        
        else:
            return JsonResponse({
                'code':1,
                'message':'Authentication Failed'
            })    
    else:
        return JsonResponse({
            'code':1,
            'message':'Authentication Failed1'
        })
            