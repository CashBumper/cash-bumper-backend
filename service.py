import uuid
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)
REQUESTER = 'requester'
GIVER = 'giver'
SESSION_TTL = 5 * 60

def make_session(_id, _type):
    return _id + '::' + _type


def session_exists(_id, _type):
    return not (r.get(make_session(_id, _type)) is None)


def save_session(_id, _type):
    r.setex(make_session(_id, _type), SESSION_TTL, '')


def requester_session_exits(_id):
    return session_exists(_id, REQUESTER)


def giver_session_exits(_id):
    return session_exists(_id, GIVER)


def create_requester_session():
    _id = str(uuid.uuid4())
    save_session(_id, REQUESTER)
    return {'id': _id}


def create_giver_session():
    _id = str(uuid.uuid4())
    save_session(_id, GIVER)
    return {'id': _id}


