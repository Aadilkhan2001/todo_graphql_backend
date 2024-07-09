import graphene

from resolvers.todo import (Resolver as TodoResolver)
from resolvers.auth import (Resolver as AuthResolver)
from mutations.todo import (Mutation as TodoMutation)

todo_route_schema = graphene.Schema(query=TodoResolver, mutation=TodoMutation)
auth_route_schema = graphene.Schema(query=AuthResolver)