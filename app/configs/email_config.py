import os
from dotenv import load_dotenv
load_dotenv()

MAIL_USERNAME = os.getenv("MAIL_USERNAME")  
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")    
MAIL_SERVER = os.getenv("MAIL_SERVER")
MAIL_FROM_NAME = os.getenv("MAIL_FROM_NAME")
MAIL_FROM = os.getenv("MAIL_FROM")        
MAIL_PORT = int(os.getenv("MAIL_PORT"))       
MAIL_STARTTLS = os.getenv("MAIL_TLS") == 'False'  
MAIL_SSL_TLS = os.getenv("MAIL_SSL") == 'True'