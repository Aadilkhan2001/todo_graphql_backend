import graphene

from bson import ObjectId
from flask import g
from datetime import datetime

from models.todo import TodoModel
from exceptions.todo import (TodoNotCreatedException,
                             TodoNotUpdatedException,
                             TodoNotDeletedException,
                             TodoNotFoundException)

class CreateTodoMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        time = graphene.String(required=True)

    response = graphene.String()
    error = graphene.String()

    def mutate(self, info, title, description, time):
        try:
          todo = TodoModel(title=title,
                           description=description,
                           time=time,
                           created_by=g.user,
                           updated_by=g.user)
          result = todo.create()
          if result:
            return CreateTodoMutation(response=f'Todo "{title}" created successfully.')
        except TodoNotCreatedException as e:
           info.context.status_code = e.status_code
           return CreateTodoMutation(error=e.message)

class UpdateTodoMutation(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)
        title = graphene.String()
        description = graphene.String()
        time = graphene.String()
        image = graphene.String()

    response = graphene.String()
    error = graphene.String()

    def mutate(self, info, id, title=None, time=None, description=None):
        try:
            update_fields = {'updated_by': g.user, 'updated_at': datetime.now()}
            if title:
                update_fields['title'] = title
            if description:
                update_fields['description'] = description
            if time:
                update_fields['time'] = time                
            result = TodoModel.update(ObjectId(id), update_fields)
            if result:
                return UpdateTodoMutation(response=f'Todo "{id}" updated successfully.')
        except TodoNotFoundException as e:
           info.context.status_code = e.status_code
           return UpdateTodoMutation(error=e.message)
        except TodoNotUpdatedException as e:
           info.context.status_code = e.status_code
           return UpdateTodoMutation(error=e.message)

class DeleteTodoMutation(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)

    response = graphene.String()
    error = graphene.String()

    def mutate(self, info, id):
        try:
            success = TodoModel.delete(ObjectId(id))
            if success:
                return DeleteTodoMutation(response=f'Todo "{id}" deleted successfully.')
        except TodoNotFoundException as e:
           info.context.status_code = e.status_code
           return DeleteTodoMutation(error=e.message)
        except TodoNotDeletedException as e:
           info.context.status_code = e.status_code
           return DeleteTodoMutation(error=e.message)

class Mutation(graphene.ObjectType):
    create_todo = CreateTodoMutation.Field()
    update_todo = UpdateTodoMutation.Field()
    delete_todo = DeleteTodoMutation.Field()