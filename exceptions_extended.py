from flask import jsonify

class InvalidUsage(Exception):

    def __init__(self, message):
        Exception.__init__(self)
        self.message = message
        self.status_code = 400

    def to_dict(self):
        rv = dict()
        rv['message'] = self.message
        return rv
