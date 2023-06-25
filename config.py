import os
# from app import ENV
from dotenv import load_dotenv

load_dotenv() # Cargar variables de entorno desde el archivo .env

class ENV:
    DB_CONNECTION = os.getenv('DB_CONNECTION', 'mysql' )
    DB_HOST = os.getenv('DB_HOST', '127.0.0.1' )
    DB_DATABASE = os.getenv('DB_DATABASE', 'api_flask' )
    DB_USERNAME = os.getenv('DB_USERNAME', 'root' )
    DB_PASSWORD = os.getenv('DB_PASSWORD', '' )
    APP_URL = os.getenv('APP_URL', 'http://127.0.0.1:5000' )
    
class DevelopmentConfig():
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'api_flask'
    
config = {
    'development': DevelopmentConfig
}