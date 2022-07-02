from passlib.context import CryptContext

pwd_context = CryptContext( schemes=['bcrypt'], deprecated="auto")

def hash_function(password: str):
    return pwd_context.hash(password)

def verify_password(attempted_password, password):
    return pwd_context.verify( attempted_password, password)
  