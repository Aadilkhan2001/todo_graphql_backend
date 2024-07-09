import requests
from logging import getLogger
from flask import g

from config import config

logger = getLogger (__name__)

class KeycloakService:
    def create_token(self, auth_code, redirect_uri):
        token_url = f"{config.keycloak_server_url}/realms/{config.keycloak_realm}/protocol/openid-connect/token"
        payload = {
            'client_id': config.keycloak_client_id,
            'client_secret': config.keycloak_client_secret,
            'code': auth_code,
            'redirect_uri': redirect_uri,
            'grant_type': 'authorization_code',
        }
        try:
            response = requests.post(token_url, data=payload)
            if response.status_code == 200:
                token_info = response.json()
                return token_info.get('access_token')
            else:
                return None
        except Exception as e:
            logger.exception(e)
            return None

    def verify_token(self, token):
        try:
            headers = {'Content-Type': 'application/x-www-form-urlencoded',}
            data = {
                'client_id': config.keycloak_client_id,
                'client_secret': config.keycloak_client_secret,
                'token': token,
            }
            verify_token_url = f'{config.keycloak_server_url}/realms/{config.keycloak_realm}/protocol/openid-connect/token/introspect'
            response = requests.post(verify_token_url, headers=headers, data=data, verify=False)
            if response.status_code == 200:
                response_data = response.json()
                if response_data.get('active'):
                    g.user = response_data.get('email')
                    return True
                else:
                    return False
        except Exception as e:
            logger.exception(e)
            return False

keycloak_service = KeycloakService()