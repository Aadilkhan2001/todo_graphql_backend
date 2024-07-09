import graphene

class TodoSchema(graphene.ObjectType):
    _id=graphene.String()
    title = graphene.String()
    description = graphene.String()
    time = graphene.String()
    created_at = graphene.DateTime()
    updated_at = graphene.DateTime()
    created_by = graphene.String()
    updated_by = graphene.String()