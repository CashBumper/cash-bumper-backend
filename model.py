import redis
import json
import uuid

# REDIS
r = redis.StrictRedis(host='localhost', port=6379, db=0)

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
def make_requester(id, latitude, longitude, transaction_id, card_number,
                   expiry_month, expiry_year, cvc, amount, range):
    return {
        'id': id,
        'latitude': latitude,
        'longitude': longitude,
        'transaction_id': transaction_id,
        'card_number': card_number,
        'expiry_month': expiry_month,
        'expiry_year': expiry_year,
        'cvc': cvc,
        'amount': amount,
        'range': range
    }

def save_requester(requester):
    r.set('requester.' + requester['id'], serialize(requester))

def load_requester(id):
    return deserialize(r.get('requester.' + id))

def load_all_requesters():
    return matching('requester.*')

def delete_requester(id):
    r.delete('requester.' + id)

## TRANSACTION
def make_transaction(id, requester_id, giver_id, amount, state='UNSEEN'):
    return {
        'id': id,
        'requester_id': requester_id,
        'giver_id': giver_id,
        'amount': amount,
        'state': state
    }

def save_transaction(transaction):
    r.set('transaction.' + transaction['id'], serialize(transaction))

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
    r.set('giver.' + giver['id'], serialize(giver))

def load_giver(id):
    print 'giver.' + id
    return deserialize(r.get('giver.' + id))

def load_all_givers():
    return matching('giver.*')

def delete_giver(id):
    r.delete('giver.' + id)
