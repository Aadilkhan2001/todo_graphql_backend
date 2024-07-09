import os

from dotenv import load_dotenv
from urllib.parse import quote_plus
from pymongo import MongoClient

load_dotenv()

class Config:
    def __init__(self) -> None:
        self.db_name = os.getenv('DATABASE_NAME')
        self.db_password = os.getenv('DATABASE_PASSWORD')
        self.db_user = os.getenv('DATABASE_USER')
        self.db_host = os.getenv('DATABASE_HOST')
        self.keycloak_server_url = os.getenv('KEYCLOAK_SERVER_URL')
        self.keycloak_client_id = os.getenv('KEYCLOAK_CLIENT_ID')
        self.keycloak_realm = os.getenv('KEYCLOAK_REALM')
        self.keycloak_client_secret = os.getenv('KEYCLOAK_SECRET')
        
    def make_db_connection_string(self):
        username = quote_plus(self.db_user)
        password = quote_plus(self.db_password)
        return f'mongodb+srv://{username}:{password}@{self.db_host}/{self.db_name}?retryWrites=true&w=majority&appName=Cluster0'
    
    def build_config(self):
        config = {
            'MONGO_URI': self.make_db_connection_string(),
            'SECRET_KEY': os.getenv('SECRET_KEY'),
        }
        return config

    def get_db(self):
        return MongoClient(self.make_db_connection_string()).get_database()

config = Config()