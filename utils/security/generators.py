import jwt
from django.conf import settings
from datetime import  timedelta, datetime
from accounts.models import *


def _generate_jwt_token():
    dt = datetime.now() + timedelta(days=60)
    token = jwt.encode({
        'id': 0,
        'exp': int(dt.strftime('%s'))
    }, settings.SECRET_KEY, algorithm='HS256')

    return token.decode('utf-8')


def token_generator():
    result = _generate_jwt_token
    token_exists = UserModel.objects.filter(token=result).exists()
    while token_exists is True:
        result = _generate_jwt_token
    else:
        return _generate_jwt_token()

def generate_account_id():
    pass