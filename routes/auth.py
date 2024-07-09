from flask import Blueprint
from flask_graphql import GraphQLView

from schemas import auth_route_schema

auth_route = Blueprint('auth_route', __name__)

auth_route.add_url_rule('/auth', view_func=GraphQLView.as_view('auth',
                                                                schema=auth_route_schema,
                                                                graphiql=True))