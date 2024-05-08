import mysql.connector
from core.config import settings

def connectToDatabase():
    return mysql.connector.connect(**settings)