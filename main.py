import service
import model
from exceptions_extended import InvalidUsage

from flask import Flask
from flask import request
from flask import jsonify

def stringify(dic):
    return jsonify(**dic)

app = Flask(__name__)
app.debug = True

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.route('/create_requester_session', methods=['POST'])
def create_requester_session():
    card_number  = request.args.get('card_number')
    expiry_month = request.args.get('expiry_month')
    expiry_year  = request.args.get('expiry_year')
    cvc          = request.args.get('cvc')
    amount       = request.args.get('amount')
    range        = request.args.get('range')

    requester = service.initiate_requester(card_number, expiry_month,
                                           expiry_year, cvc, amount, range)

    print requester
    return stringify(requester)


@app.route('/create_giver_session', methods=['POST'])
def create_giver_session():
    amount = request.args.get('amount')
    range  = request.args.get('range')
    sepa   = request.args.get('sepa')
    giver  = service.initialize_giver(amount, range, sepa)

    print giver
    return stringify(giver)


@app.route('/find_givers_around', methods=['GET'])
def find_givers_near():
    latitude     = request.args.get('lat')
    longitude    = request.args.get('lng')
    requester_id = request.args.get('requester_id')

    givers       = service.find_givers_near(requester_id, latitude, longitude)

    print givers
    return stringify({'givers': givers})


@app.route('/find_requesters_around', methods=['GET'])
def find_requesters_near():
    latitude   = request.args.get('lat')
    longitude  = request.args.get('lng')
    giver_id   = request.args.get('giver_id')
    requesters = service.find_requesters_near(giver_id, latitude, longitude)

    print requesters
    return stringify({'requesters': requesters})


@app.route('/accept_request', methods=['GET'])
def accept_request():
    requester_id = request.args.get('requester_id')
    giver_id     = request.args.get('giver_id')
    service.accept_request(requester_id, giver_id)
    return ''

@app.route('/get_requester_transaction_giver', methods=['GET'])
def requester_transaction():
    requester_id = request.args.get('requester_id')
    transaction  = model.load_transaction_by_requester(requester_id)
    giver        = model.load_giver(transaction.giver_id)

    print giver
    return giver

@app.route('/bump', methods=['POST'])
def bump():
    requester_id = request.args.get('requester_id')
    service.set_transaction_state(requester_id, 'CONFIRMED')
    service.transfer_to_giver(requester_id)
    service.clean_up(requester_id)
    return ''


if __name__ == '__main__':
    app.run(host='172.20.19.51')
