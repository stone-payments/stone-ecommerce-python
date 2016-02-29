def create_creditcard_request(**kwargs):
 
        request = {
            'BillingAddress': kwargs.get('billing_address'),
            'CreditCardBrand': kwargs.get('creditcard_brand'),
            'CreditCardNumber': kwargs.get('creditcard_number'),
            'ExpMonth': kwargs.get('exp_month'),
            'ExpYear': kwargs.get('exp_year'),
            'HolderName': kwargs.get('holder_name'),
            'IsOneDollarAuthEnabled': kwargs.get('is_one_dollar_auth_enabled') or 'false',
            'SecurityCode': kwargs.get('security_code')
        }
        return request
	