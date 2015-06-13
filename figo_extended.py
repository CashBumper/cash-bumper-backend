import figo

def make_payment(session, account, amount):
    payment = figo.Payment(session)
    payment.account_id = 'A1.1'
    payment.type = 'Transfer'
    payment.account_number = '4711951501'
    payment.purpose = 'Please work :*'
    payment.bank_code = '90090042'
    payment.name = 'cash bumber'
    payment.amount = int(float(amount))

    return payment

def pay(account, amount):
    session = figo.FigoSession('ASHWLIkouP2O6_bgA2wWReRhletgWKHYjLqDaqb0LFfamim9RjexTo22ujRIP_cjLiRiSyQXyt2kM1eXU2XLFZQ0Hro15HikJQT_eNeT_9XQ')
    payment = make_payment(session, account, amount)
    session.add_payment(payment)
