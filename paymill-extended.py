import paymill
import requests

PUBKEY = '95483231163ca57c2678ee1c32e220a9'
PRIVKEY = 'c1639092ab86cb87d83b6b9118fe1e41'

def create_token(number, expiry_month, expiry_year, cvc, holdername, amount, currency):
    r = requests.get('https://test-token.paymill.de', params={
        'transaction.mode': 'CONNECTOR_TEST',
        'channel.id': PUBKEY,
        'account.number': number,
        'account.expiry.month': expiry_month,
        'account.expiry.year': expiry_year,
        'account.holder': holdername,
        'presentation.amount3D': amount,
        'presentation.currency3D': currency
    })

    return r.json()['transaction']['identification']['uniqueId']

paymill_context = paymill.PaymillContext(PRIVKEY)
transaction_service = paymill_context.get_transaction_service()

def pay(number, expiry_month, expiry_year, cvc, holdername, amount):
    token = create_token(number, expiry_month, expiry_year, cvc, holdername,
                         amount, 'EUR')

    return transaction_service.create_with_token(
        token=token,
        amount=amount,
        currency='EUR',
        description='It works!'
    )
