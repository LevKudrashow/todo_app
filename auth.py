from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt

SECRET_KEY = "your_secret_key_here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Initialize CryptContext for password hashing
pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.hashed_password = get_password_hash(password)

def get_password_hash(password: str):
    return pwd_cxt.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_cxt.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def authenticate_user(username: str, password: str):
    # Test user for checking purposes.
    if username == "testuser" and password == "testpassword":
        return User(username=username, password=password)
    return None