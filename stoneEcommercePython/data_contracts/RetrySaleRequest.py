from uuid import UUID


def retry_sale_request(**kwargs):
    request = {
        'RequestKey': kwargs.get('request_key') or UUID("00000000-0000-0000-0000-000000000000"),
        'OrderKey': kwargs.get('order_key') or UUID("00000000-0000-0000-0000-000000000000"),
        'Options': kwargs.get('retry_sale_options'),
        'RetrySaleCreditCardTransactionCollection': kwargs.get('retry_sale_creditcard_transaction_collection')
    }
    return request


def retry_sale_options(**kwargs):
    options ={
        'ExtendedLimitEnabled': kwargs.get('extended_limit_enabled'),
        'ExtendedLimitCode': kwargs.get('extended_limit_code')
    }
    return options


def retry_sale_creditcard_transaction(**kwargs):
    transaction = {
        'TransactionKey': kwargs.get('transaction_key'),
        'SecurityCode': kwargs.get('security_code')
    }
    return transaction