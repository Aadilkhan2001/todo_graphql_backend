import graphene

from bson import ObjectId
from flask import g

from models.todo import TodoModel
from schemas.todo import TodoSchema
from exceptions.todo import TodoNotFoundException

class Resolver(graphene.ObjectType):
    todos = graphene.List(TodoSchema)
    get_todo_by_id = graphene.Field(TodoSchema, id=graphene.String(required=True))

    error = graphene.String()

    def resolve_todos(self, info):
        return list(TodoModel.list_all(g.user))

    def resolve_get_todo_by_id(self, info, id):
        try:
          todo = TodoModel.get_by_id(id=(ObjectId(id)))
          if todo:
             return todo
        except TodoNotFoundException as e:
           info.context.status_code = e.status_code
           return Resolver(error=e.message)