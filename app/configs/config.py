import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

ACCESS_TOKEN_EXPIRY = os.getenv("ACCESS_TOKEN_EXPIRY")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

MAIL_USERNAME = os.getenv("MAIL_USERNAME")  
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")    
MAIL_SERVER = os.getenv("MAIL_SERVER")
MAIL_FROM_NAME = os.getenv("MAIL_FROM_NAME")
MAIL_FROM = os.getenv("MAIL_FROM")        
MAIL_PORT = int(os.getenv("MAIL_PORT"))       
MAIL_TLS = os.getenv("MAIL_TLS") == 'True'  
MAIL_SSL = os.getenv("MAIL_SSL") == 'False'