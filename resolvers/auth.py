import graphene

from config import config
from services.keycloak import keycloak_service

class Resolver(graphene.ObjectType):
    login_url = graphene.String(redirect_uri=graphene.NonNull(graphene.String))
    token = graphene.String(code=graphene.NonNull(graphene.String), redirect_uri=graphene.NonNull(graphene.String))

    def resolve_login_url(self, info, redirect_uri):
        login_url = (
            f"{config.keycloak_server_url}/realms/{config.keycloak_realm}/protocol/openid-connect/auth"
            f"?client_id={config.keycloak_client_id}"
            f"&redirect_uri={redirect_uri}"
            f"&response_type=code"
            f"&scope=openid profile"
        )
        return login_url
    
    def resolve_token(self, info, code, redirect_uri):
        token = keycloak_service.create_token(code, redirect_uri)
        return token