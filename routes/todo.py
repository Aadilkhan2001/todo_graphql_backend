from flask import Blueprint
from flask_graphql import GraphQLView

from schemas import todo_route_schema
from middleware.keycloak import keycloak_protected

todo_route = Blueprint('todo_route', __name__)

protected_view = keycloak_protected(GraphQLView.as_view('todo',
                                                        schema=todo_route_schema,
                                                        graphiql=True))

todo_route.add_url_rule('/todo', view_func=protected_view)