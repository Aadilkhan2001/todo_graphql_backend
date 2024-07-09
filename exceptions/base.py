class BaseException(Exception):
    def __init__(self, message, status_code):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        return {'message': self.message, 'status_code': self.status_code}