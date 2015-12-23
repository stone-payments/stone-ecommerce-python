from uuid import UUID


def create_sale_request(**kwargs):
    if kwargs.get('creditcard_transaction_collection') or kwargs.get('boleto_transaction_collection'):
        request = {
            'RequestKey': kwargs.get('request_key') or UUID("00000000-0000-0000-0000-000000000000"),
            'CreditCardTransactionCollection': kwargs.get('creditcard_transaction_collection'),
            'BoletoTransactionCollection': kwargs.get('boleto_transaction_collection'),
            'Order': kwargs.get('order'),
            'Buyer': kwargs.get('buyer'),
            'ShoppingCartCollection': kwargs.get('shopping_cart_collection'),
            'Options': kwargs.get('options'),
            'Merchant': kwargs.get('merchant'),
            'RequestData': kwargs.get('request_data')
        }
        return request
    else:
        raise UserWarning('The request must contain at least one transaction')


def boleto_transaction(amount_in_cents, **kwargs):
    transaction = {
        'AmountInCents': amount_in_cents,
        'BankNumber': kwargs.get('bank_number'),
        'Instructions': kwargs.get('instructions'),
        'DocumentNumber': kwargs.get('document_number'),
        'TransactionReference': kwargs.get('transaction_reference'),
        'BillingAddress': kwargs.get('billing_address'),
        'TransactionDateInMerchant': kwargs.get('transaction_date_in_merchant'),
        'Options': kwargs.get('options')
    }
    return transaction


def billing_address(**kwargs):
    address = {
        'Country': kwargs.get('country'),
        'State': kwargs.get('state'),
        'City': kwargs.get('city'),
        'District': kwargs.get('district'),
        'Street': kwargs.get('street'),
        'Number': kwargs.get('number'),
        'Complement': kwargs.get('complement'),
        'ZipCode': kwargs.get('zip_code')
    }
    return address


def boleto_transaction_options(currency_iso, days_to_add_in_boleto_expiration_date=None):
    options = {
        'DaysToAddInBoletoExpirationDate': days_to_add_in_boleto_expiration_date,
        'CurrencyIsoField': currency_iso
    }
    return options


def creditcard_transaction(amount_in_cents, creditcard, creditcard_operation='AuthAndCapture', **kwargs):
    transaction = {
        'CreditCard': creditcard,
        'Options': kwargs.get('options'),
        'Recurrency': kwargs.get('recurrency'),
        'AmountInCents': amount_in_cents,
        'InstallmentCount': kwargs.get('installment_count') or 0,
        'CreditCardOperation': creditcard_operation,
        'TransactionReference': kwargs.get('transaction_reference'),
        'TransactionDateInMerchant': kwargs.get('transaction_date_in_merchant')
    }
    return transaction


def creditcard(creditcard_number, creditcard_brand, exp_month, exp_year, holder_name, security_code,
               billing_address=None):
    card = {
        'CreditCardNumber': creditcard_number,
        'HolderName': holder_name,
        'SecurityCode': security_code,
        'ExpMonth': exp_month,
        'ExpYear': exp_year,
        'CreditCardBrand': creditcard_brand,
        'BillingAddress': billing_address
    }
    return card
	
	
def creditcard_instant_buy(instant_buy_key, billing_address=None):
    card = {
        'InstantBuyKey': instant_buy_key or UUID("00000000-0000-0000-0000-000000000000"),
        'BillingAddress': billing_address
    }
    return card


def creditcard_transaction_options(**kwargs):
    options = {
        'PaymentMethodCode': kwargs.get('payment_method_code'),
        'IataAmountInCents': kwargs.get('iata_amount_in_cents') or 0,
        'CaptureDelayInMinutes': kwargs.get('capture_delay_in_minutes') or 0,
        'MerchantCategoryCode': kwargs.get('merchant_category_code'),
        'SoftDescriptorText': kwargs.get('soft_descriptor_text'),
        'InterestRate': kwargs.get('interest_rate'),
        'ExtendedLimitEnabled': kwargs.get('extended_limit_enabled'),
        'ExtendedLimitCode': kwargs.get('extended_limit_code'),
        'CurrencyIso': kwargs.get('currency_iso')
    }
    return options


def recurrency(frequency, interval, date_to_start_billing, recurrences, one_dollar_auth):
    recurrency_dict = {
        'Frequency': frequency,
        'Interval': interval,
        'DateToStartBilling': date_to_start_billing,
        'Recurrences': recurrences,
        'OneDollarAuth': one_dollar_auth
    }
    return recurrency_dict


def order(order_reference):
    order_dict = {
        'OrderReference': order_reference
    }
    return order_dict


def buyer(document_number, document_type, name, person_type, **kwargs):
    buyer_dict = {
        "AddressCollection": kwargs.get('address_collection'),
        "Birthdate": kwargs.get('birth_date'),
        "DocumentNumber": document_number,
        "DocumentType": document_type,
        "Email": kwargs.get('email'),
        "EmailType": kwargs.get('email_type'),
        "FacebookId": kwargs.get('facebook_id'),
        "Gender": kwargs.get('gender'),
        "HomePhone": kwargs.get('home_phone'),
        "MobilePhone": kwargs.get('mobile_phone'),
        "Name": name,
        "PersonType": person_type,
        "TwitterId": kwargs.get('twitter_id'),
        "WorkPhone": kwargs.get('work_phone'),
        "BuyerCategory": kwargs.get('buyer_category'),
        "BuyerKey": kwargs.get('buyer_key') or UUID("00000000-0000-0000-0000-000000000000"),
        "BuyerReference": kwargs.get('buyer_reference'),
        "CreateDateInMerchant": kwargs.get('create_date_in_merchant'),
        "LastBuyerUpdateInMerchant": kwargs.get('last_buyer_update_in_merchant')
    }
    return buyer_dict


def buyer_address(**kwargs):
    address = {
        'Country': kwargs.get('country'),
        'State': kwargs.get('state'),
        'City': kwargs.get('city'),
        'District': kwargs.get('district'),
        'Street': kwargs.get('street'),
        'Number': kwargs.get('number'),
        'Complement': kwargs.get('complement'),
        'ZipCode': kwargs.get('zip_code'),
        'AddressType': kwargs.get('address_type')
    }
    return address


def merchant(merchant_reference):
    merchant_data = {
        "MerchantReference": merchant_reference
    }
    return merchant_data


def sale_options(**kwargs):
    options = {
        'IsAntiFraudEnabled': kwargs.get('is_anti_fraud_enabled'),
        'AntiFraudServiceCode': kwargs.get('anti_fraud_service_code') or 0,
        'Retries': kwargs.get("retries"),
        'CurrencyIso': kwargs.get('currency_iso_field')
    }
    return options


def request_data(**kwargs):
    data = {
        "EcommerceCategory": kwargs.get('ecommerce_category'),
        "IpAddress": kwargs.get('ip_address'),
        "Origin": kwargs.get('origin'),
        "SessionId": kwargs.get('session_id')
    }
    return data


def shopping_cart(**kwargs):
    cart = {
        "DeliveryAddress": kwargs.get('delivery_address'),
        "DeliveryDeadline": kwargs.get('delivery_deadline'),
        "EstimatedDeliveryDate": kwargs.get('estimated_delivery_date'),
        "FreightCostInCents": kwargs.get('freight_cost_in_cents'),
        "ShippingCompany": kwargs.get('shipping_company'),
        "ShoppingCartItemCollection": kwargs.get('shopping_cart_item_collection')
    }
    return cart


def delivery_address(**kwargs):
    address = {
        'Country': kwargs.get('country'),
        'State': kwargs.get('state'),
        'City': kwargs.get('city'),
        'District': kwargs.get('district'),
        'Street': kwargs.get('street'),
        'Number': kwargs.get('number'),
        'Complement': kwargs.get('complement'),
        'ZipCode': kwargs.get('zip_code')
    }
    return address


def shopping_cart_item(**kwargs):
    item = {
        "Description": kwargs.get('description'),
        "DiscountAmountInCents": kwargs.get('discount_amount_in_cents'),
        "ItemReference": kwargs.get('item_reference'),
        "Name": kwargs.get('name'),
        "Quantity": kwargs.get('quantity'),
        "TotalCostInCents": kwargs.get('total_cost_in_cents'),
        "UnitCostInCents": kwargs.get('unit_cost_in_cents')
    }
    return item
