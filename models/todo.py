from datetime import datetime
from bson.objectid import ObjectId
from logging import getLogger

from config import config
from exceptions.todo import (TodoNotCreatedException,
                             TodoNotUpdatedException,
                             TodoNotDeletedException,
                             TodoNotFoundException)

logger = getLogger(__name__)

class TodoModel:
    def __init__(self,
                 title,
                 description,
                 time,
                 created_by,
                 updated_by,):
        self.title = title
        self.description = description
        self.time = time
        self.created_by = created_by
        self.updated_by = updated_by

    def create(self):
        try:
            now = datetime.now()
            result = config.get_db().todos.insert_one({
            'title': self.title,
            'description': self.description,
            'time': self.time,
            'created_at': now,
            'updated_at': now,
            'created_by': self.created_by,
            'updated_by': self.updated_by,
           })
            if result:
                return result
            else:
                raise TodoNotCreatedException
        except Exception as e:
            logger.exception(e)
            raise TodoNotCreatedException

    @staticmethod
    def list_all(user):
        try:
            return list(config.get_db().todos.find({"created_by": user}))
        except Exception as e:
            logger.exception(e)
            return []

    @staticmethod
    def get_by_id(id):
        try:
            todo = config.get_db().todos.find_one({"_id": ObjectId(id)})
            if todo:
                return todo
            else:
                raise Exception
        except Exception as e:
            logger.exception(e)
            raise TodoNotFoundException

    @staticmethod
    def update(id, update_fields):
        try:
            result = config.get_db().todos.update_one(
                {"_id": ObjectId(id)},
                {"$set": update_fields})
            if result.matched_count:
                return result
            else:
                raise TodoNotFoundException
        except TodoNotFoundException as e:
            raise e
        except Exception as e:
            raise TodoNotUpdatedException

    @staticmethod
    def delete(id):
        try:
            result = config.get_db().todos.delete_one({"_id": ObjectId(id)})
            if result.deleted_count:
                return result
            else:
                raise TodoNotFoundException
        except TodoNotFoundException as e:
            raise e
        except Exception as e:
            raise TodoNotDeletedException