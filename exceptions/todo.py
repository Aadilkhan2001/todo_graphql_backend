from exceptions.base import BaseException

class TodoNotCreatedException(BaseException):
    def __init__(self):
        super().__init__('todo-not-created-error', 500)

class TodoNotFoundException(BaseException):
    def __init__(self):
        super().__init__('todo-not-found', 404)

class TodoNotUpdatedException(BaseException):
    def __init__(self):
        super().__init__('todo-not-updated-error', 500)

class TodoNotDeletedException(BaseException):
    def __init__(self):
        super().__init__('todo-not-deleted-error', 500)