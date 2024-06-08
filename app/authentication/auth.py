"""from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from fastapi import HTTPException
from app.cruds.crudUsuario import buscarUsuarioPorUser

SECRET_KEY = "laPasswordDeArquitectura001"  # Cambia esto por una clave secreta segura
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)


async def authenticate_user(user: str, password: str):
    usuario = buscarUsuarioPorUser(user)
    if not usuario:
        return None, None  # Devuelve None si el usuario no existe
    if not verify_password(password, usuario.password):
        return None, None  # Devuelve None si la contraseña no coincide
    return usuario, usuario.rol  # Devuelve el usuario y su rol"""
