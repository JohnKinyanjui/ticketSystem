import uuid
import hashlib


def hash_password(password):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashedPassword, userPassword):
    password, salt = hashedPassword.split(':')
    return password == hashlib.sha256(salt.encode() + userPassword.encode()).hexdigest()