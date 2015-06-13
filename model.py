import redis
import json
import uuid

# REDIS
r = redis.StrictRedis(host='localhost', port=6379, db=0)
SESSION_TTL = 15 * 60

def setex(key, val):
    r.setex(key, SESSION_TTL, val)

def matching(pattern):
    keys = r.keys(pattern)
    return map(lambda key: deserialize(r.get(key)), keys)

## UTILS
def deserialize(string):
    return json.loads(string)

def serialize(model):
    return json.dumps(model)

def random_id():
    return str(uuid.uuid4())

# MODEL

## REQUESTER
def make_requester(id, latitude, longitude, transaction_id, account, amount, range):
    return {
        'id': id,
        'latitude': latitude,
        'longitude': longitude,
        'transaction_id': transaction_id,
        'account': account,
        'amount': amount
    }

def save_requester(requester):
    setex('requester.' + requester['id'], serialize(requester))

def load_requester(id):
    return deserialize(r.get('requester.' + id))

def load_all_requesters():
    return matching('requester.*')

## TRANSACTION
def make_transaction(id, requester_id, state='UNSEEN'):
    return {
        'id': id,
        'requester_id': requester_id,
        'state': state
    }

def save_transaction(transaction):
    setex('transaction.' + transaction['id'], serialize(transaction))

def load_transaction(id):
    return deserialize(r.get('transaction.' + id))

def load_transaction_by_requester(requester_id):
    requester = load_requester(requester_id)
    return load_transaction(requester['transaction_id'])

def load_all_transactions():
    return matching('transactions.*')

## GIVER
def make_giver(id, latitude, longitude, amount, range, sepa):
    return {
        'id': id,
        'latitude': latitude,
        'longitude': longitude,
        'amount': amount,
        'range': range,
        'sepa': sepa
    }

def save_giver(giver):
    setex('giver.' + giver['id'], serialize(giver))

def load_giver(id):
    return deserialize(r.get('giver.' + id))

def load_all_givers():
    return matching('givers.*')
