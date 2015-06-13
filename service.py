import model

def initiate_requester(amount, range, account):
    transaction_id = model.random_id()
    requester_id = model.random_id()

    transaction = model.make_transaction(transaction_id, requester_id, None)
    requester = model.make_requester(requester_id, 0, 0, transaction_id,
                                     account, amount, range)

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
    transaction.state = state
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
