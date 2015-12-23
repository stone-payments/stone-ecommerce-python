from uuid import UUID


def manage_sale_request(**kwargs):
    request = {
        'RequestKey': kwargs.get('request_key') or UUID("00000000-0000-0000-0000-000000000000"),
        'CreditCardTransactionCollection': kwargs.get('creditcard_transaction_collection'),
        'OrderKey': kwargs.get('order_key') or UUID("00000000-0000-0000-0000-000000000000")
    }
    return request


def manage_creditcard_transaction(**kwargs):
    transaction = {
        'TransactionKey': kwargs.get('transaction_key') or UUID("00000000-0000-0000-0000-000000000000"),
        'TransactionReference': kwargs.get('transaction_reference'),
        'AmountInCents': kwargs.get('amount_in_cents') or 0
    }