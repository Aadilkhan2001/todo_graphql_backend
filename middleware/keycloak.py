from logging import getLogger
from functools import wraps
from flask import request, jsonify

from services.keycloak import keycloak_service

logger = getLogger(__name__)

def keycloak_protected(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        authorization_header = request.headers.get('Authorization', None)
        try:
          if authorization_header:
              token = authorization_header.split(' ')[1]
              is_token_verified = keycloak_service.verify_token(token)
              if is_token_verified:
                  return func(*args, **kwargs)
              else:
                  return jsonify({'error': 'Invalid token'}), 401              
          else:
              return jsonify({'error': 'Authentication token required'}), 401
        except Exception as e:
            logger.exception(e)
            return jsonify({'error': 'Authentication token required'}), 401
    return wrapper