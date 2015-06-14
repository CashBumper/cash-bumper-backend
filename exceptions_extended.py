from flask import jsonify

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        rv = dict()
        rv['message'] = self.message
        return rv
