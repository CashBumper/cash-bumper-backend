import model
import paymill_extended
import figo_extended

def initiate_requester(card_number, expiry_month, expiry_year, cvc, amount,
                       range):
    transaction_id = model.random_id()
    requester_id = model.random_id()

    transaction = model.make_transaction(transaction_id, requester_id, None,
                                         amount)
    requester = model.make_requester(requester_id, 0, 0, transaction_id,
                                     card_number, expiry_month, expiry_year,
                                     cvc, amount, range)

    model.save_transaction(transaction)
    model.save_requester(requester)

    return {'requester_id': requester_id, 'transaction_id': transaction_id}

def initialize_giver(amount, range, sepa):
    giver_id = model.random_id()
    giver = model.make_giver(giver_id, 0, 0, amount, range, sepa)
    model.save_giver(giver)

    return {'id': giver_id}

def set_transaction_state(requester_id, state):
    transaction = model.load_transaction_by_requester(requester_id)
    transaction['state'] = state
    model.save_transaction(transaction)

def update_location(object, latitude, longitude):
    object['latitude']  = latitude
    object['longitude'] = longitude

def find_requesters_near(giver_id, latitude, longitude):
    giver = model.load_giver(giver_id)
    update_location(giver, latitude, longitude)
    model.save_giver(giver)

    return model.load_all_requesters()

def find_givers_near(requester_id, latitude, longitude):
    requester = model.load_requester(requester_id)
    update_location(requester, latitude, longitude)
    model.save_requester(requester)

    return model.load_all_givers()

def transfer_from_requester(requester_id):
    requester = model.load_requester(requester_id)
    paymill_extended.pay(
        requester['card_number'],
        requester['expiry_month'],
        requester['expiry_year'],
        requester['cvc'],
        'requester',
        requester['amount']
    )

def transfer_to_giver(requester_id):
    transaction = model.load_transaction_by_requester(requester_id)
    giver = model.load_giver(transaction['giver_id'])
    figo_extended.pay(giver['sepa'], transaction['amount'])

def set_transaction_giver(requester_id, giver_id):
    transaction = model.load_transaction_by_requester(requester_id)
    transaction['giver_id'] = giver_id
    model.save_transaction(transaction)

def accept_request(requester_id, giver_id):
    set_transaction_state(requester_id, 'ACCEPTED')
    set_transaction_giver(requester_id, giver_id)
    transfer_from_requester(requester_id)
