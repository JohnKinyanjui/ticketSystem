from django.http import JsonResponse
from utils.security.generators import *
from utils.security.utils import check_password, hash_password
from security.models import SystemUser


def create_account(userToken ,userImage, fullName, password, role):
    if SystemUser.objects.filter(token=userToken).exists() is False:
        return JsonResponse({
            'code': 1,
            'message': 'Permission Denied'
        })

    accountId = generate_account_id(role)
    userModel = UserModel(
        userId=accountId,
        userImage=userImage,
        fullName=fullName,
        password=hash_password(password),
        role=role
    )
    userModel.save()
    return JsonResponse({
        'code': 0,
        'accountId': accountId,
        'message': 'Account created'
    })

def create_mtn_account(userToken ,userImage, fullName, password, role):
    if UserModel.objects.filter(token=userToken, role="Field Manager").exists() is False:
        return JsonResponse({
            'code': 1,
            'message': 'Permission Denied'
        })

    accountId = generate_account_id()
    userModel = UserModel(
        userId=accountId,
        userImage=userImage,
        fullName=fullName,
        password=password,
        role=role
    )
    userModel.save()
    return JsonResponse({
        'code': 0,
        'message': 'Account created'
    })


def authenticate_account(userId, userPassword):
    if UserModel.objects.filter(userId=userId).exists():
        user = UserModel.objects.get(userId=userId)
        if check_password(user.password, userPassword):
            token = token_generator()
            UserModel.objects.filter(id=user.id).update(token=token)
            return JsonResponse({
                'code': 0,
                'token': token,
                'message': "Authentication Successful"
            })
        return JsonResponse({
            'code': 1,
            'token': '',
            'message': 'Authentication Failed'
        })
    else:
        return JsonResponse({
            'code': 1,
            'message': 'Authentication Failed'
        })


def get_field_agents(userToken):
    if UserModel.objects.filter(token=userToken, role="Field Manager"):
        agents = UserModel.objects.filter(role="Field Agents").all().values()
        return JsonResponse({
            "code": 0,
            "agents": list(agents)
        })
    else:
        return JsonResponse({
            'code': 1,
            'agents': []
        })
