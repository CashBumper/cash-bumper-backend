
from flask import Flask
from flask import request

app = Flask(__name__)
app.debug = True


@app.route('/create_requester_session', methods=['POST'])
def create_requester_session():
    amount = request.args.get('amount')
    account = request.args.get('account')

    return '/create_requester_session?amount=%s&account=%s' % (amount, account)


@app.route('/create_giver_session', methods=['POST'])
def create_giver_session():
    max_amount = request.args.get('max_amount')
    max_range = request.args.get('max_range')
    sepa = request.args.get('sepa')

    return '/create_giver_session?max_amount=%s&max_range=%s&sepa=%s' % (max_amount, max_range, sepa)


@app.route('/find_givers_around', methods=['GET'])
def find_givers_around():
    latitude = request.args.get('lat')
    longitude = request.args.get('lng')

    return '/find_givers_around?lat=%s&lng=%s' % (latitude, longitude)


@app.route('/find_requesters_around', methods=['GET'])
def find_requesters_around():
    latitude = request.args.get('lat')
    longitude = request.args.get('lng')

    return '/find_requesters_around?lat=%s&lng=%s' % (latitude, longitude)


@app.route('/saw_request', methods=['GET'])
def saw_request():
    giver_id = request.args.get('id')
    requester_id = request.args.get('requester_id')

    return '/saw_request?id=%s&requester_id=%s' % (giver_id, requester_id)


@app.route('/accept_request', methods=['GET'])
def accept_request():
    giver_id = request.args.get('id')
    requester_id = request.args.get('requester_id')

    return '/accept_request?id=%s&requester_id=%s' % (giver_id, requester_id)


@app.route('/reject_request', methods=['GET'])
def reject_request():
    giver_id = request.args.get('id')
    requester_id = request.args.get('requester_id')

    return '/reject_request?id=%s&requester_id=%s' % (giver_id, requester_id)


@app.route('/bump', methods=['POST'])
def bump():
    bumper_id = request.args.get('id')
    requester_id = request.args.get('requester_id')
    giver_id = request.args.get('giver_id')

    if requester_id is None:
        return '/bump?bumper_id=%s&giver_id=%s' % (bumper_id, giver_id)
    else:
        return '/bump?bumper_id=%s&requester_id=%s' % (bumper_id, requester_id)


if __name__ == '__main__':
    app.run(host='172.20.19.51')
