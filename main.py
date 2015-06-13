import service
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)
app.debug = True


@app.route('/create_requester_session', methods=['POST'])
def create_requester_session():
    amount = request.args.get('amount')
    account = request.args.get('account')

    _id = service.create_requester_session()
    return jsonify(**_id)


@app.route('/create_giver_session', methods=['POST'])
def create_giver_session():
    max_amount = request.args.get('max_amount')
    max_range = request.args.get('max_range')
    sepa = request.args.get('sepa')

    _id = service.create_giver_session()
    return jsonify(**_id)


@app.route('/find_givers_around', methods=['GET'])
def find_givers_around():
    latitude = request.args.get('lat')
    longitude = request.args.get('lng')

    return '{}'


@app.route('/find_requesters_around', methods=['GET'])
def find_requesters_around():
    latitude = request.args.get('lat')
    longitude = request.args.get('lng')

    return '{}'


@app.route('/saw_request', methods=['GET'])
def saw_request():
    giver_id = request.args.get('id')
    transaction_id = request.args.get('transaction_id')

    valid_giver_id = service.giver_session_exists(giver_id)

    if not (valid_giver_id):
        return '', 400

    return ''


@app.route('/accept_request', methods=['GET'])
def accept_request():
    giver_id = request.args.get('id')
    transaction_id = request.args.get('transaction_id')

    valid_giver_id = service.giver_session_exists(giver_id)

    if not (valid_giver_id):
        return '', 400

    return ''


@app.route('/reject_request', methods=['GET'])
def reject_request():
    giver_id = request.args.get('id')
    transaction_id = request.args.get('transaction_id')

    valid_giver_id = service.giver_session_exists(giver_id)

    if not (valid_giver_id):
        return '', 400

    return ''


@app.route('/requester_bump', methods=['POST'])
def requester_bump():
    requester_id = request.args.get('requester_id')
    transaction_id = request.args.get('transaction_id')

    valid_requester_id = service.requester_session_exists(requester_id)

    if not(valid_requester_id):
        return '', 400

    return


@app.route('/giver_bump', methods=['POST'])
def giver_bump():
    giver_id = request.args.get('giver_id')
    transaction_id = request.args.get('transaction_id')

    valid_giver_id = service.giver_session_exists(giver_id)

    if not(valid_giver_id):
        return '', 400

    return


if __name__ == '__main__':
    app.run(host='172.20.19.51')
