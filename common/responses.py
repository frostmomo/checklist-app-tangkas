from flask import jsonify

class BaseResponse(object):

    data = None
    status = 200
    message = None

    def __init__(self, data, exception, page, limit, total, status):
        self.total = total
        self.page = page
        self.limit = limit
        self.data = data
        self.message = str(exception) if exception is not None else None
        self.status = status

    def serialize(self):
        return {
            # message / status/ data
                'data':{
                    'list': self.data,
                    "total": self.total,
                    "page": self.page,
                    "limit": self.limit
                }, 
                
            'status': self.status,
            'message': self.message,
        }
    
class SingleBaseResponse(object):
    
    data = None
    status = 200
    message = None

    def __init__(self, data, exception, status):
        self.data = data
        self.message = str(exception) if exception is not None else None
        self.status = status

    def serialize(self):
        return {
            # message / status/ data
            'data':self.data, 
            'status': self.status,
            'message': self.message,
        }
    
class ErrorResponse(object):

    data = None
    status = False
    message = None
    total = 0
    page = 0
    limit = 0
    code = 500

    def __init__(self, exception, code):
        self.message = str(exception) if exception is not None else None
        self.code = code

    def serialize(self):
        return (
            jsonify(BaseResponse(None, self.message, 0, 0, 0, 400).serialize()),
            self.code
        )