import uuid
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)
app.debug = True


def random_id_object():
    return {'id': uuid.uuid4()}


@app.route('/create_requester_session', methods=['POST'])
def create_requester_session():
    amount = request.args.get('amount')
    account = request.args.get('account')

    _id = random_id_object()
    return jsonify(**_id)


@app.route('/create_giver_session', methods=['POST'])
def create_giver_session():
    max_amount = request.args.get('max_amount')
    max_range = request.args.get('max_range')
    sepa = request.args.get('sepa')

    _id = random_id_object()
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
    requester_id = request.args.get('requester_id')

    return ''


@app.route('/accept_request', methods=['GET'])
def accept_request():
    giver_id = request.args.get('id')
    requester_id = request.args.get('requester_id')

    return ''


@app.route('/reject_request', methods=['GET'])
def reject_request():
    giver_id = request.args.get('id')
    requester_id = request.args.get('requester_id')

    return ''


@app.route('/bump', methods=['POST'])
def bump():
    bumper_id = request.args.get('id')
    requester_id = request.args.get('requester_id')
    giver_id = request.args.get('giver_id')

    if requester_id is None:
        return ''
    else:
        return ''


if __name__ == '__main__':
    app.run(host='172.20.19.51')
