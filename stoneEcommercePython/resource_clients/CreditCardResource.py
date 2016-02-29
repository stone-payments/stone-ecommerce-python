import requests
from data_contracts import create_creditcard_request
import json
from AbstractResource import AbstractResource
from uuid import UUID


class uuid_serialize(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
          return str(obj)
            # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)
		

class CreditCardResource(AbstractResource):

    def __init__(self, merchant_key=None, environment=None, http_content_type=None, host_uri=None):
        super(CreditCardResource, self).__init__(merchant_key, environment, http_content_type, "/CreditCard", host_uri)

    def __get_creditcard_data_implementation(self, key, identifier_name):
        if identifier_name:
            identifier_name = identifier_name + "="

        action_name = '/{0}{1}'.format(identifier_name, str(key))
        request_headers = {"merchantKey": str(self.merchant_key), 'Content-Type': 'application/json', 'Accept': 'application/json'}
        
        return requests.get(self.host_uri + self.resource_name + action_name, headers=request_headers)

    def get_creditcard_data(self, instant_buy_key):
        return self.__get_creditcard_data_implementation(instant_buy_key, '')

    ## metodo removido, deixado para nao quebrar clientes antigos
    def get_instant_buy_data(self, instant_buy_key):
        return self.get_creditcard_data(instant_buy_key)

    def get_creditcard_data_with_buyer_key(self, buyer_key):
        return self.__get_creditcard_data_implementation(buyer_key, 'BuyerKey')

    ## metodo removido, deixado para nao quebrar clientes antigos
    def get_instant_buy_data_with_buyer_key(self, buyer_key):
        return self.get_creditcard_data_with_buyer_key(buyer_key)

    def post_create_creditcard(self, creditcard_data_request):
        creditcard_request_header = {"MerchantKey": str(self.merchant_key), 'Content-Type': 'application/json', 'Accept': 'application/json'}
        return requests.post(self.host_uri + self.resource_name, data=json.dumps(creditcard_data_request, cls=uuid_serialize), headers = creditcard_request_header)
		
    def patch_creditcard(self, buyer_key, instant_buy_key):
        creditcard_request_header = {"MerchantKey": str(self.merchant_key), 'Content-Type': 'application/json', 'Accept': 'application/json'}
        action_name = '/' + str(instant_buy_key)
        json_buyer_key = {'BuyerKey':str(buyer_key)}
        return requests.patch(self.host_uri + self.resource_name + action_name, data = json.dumps(json_buyer_key, cls=uuid_serialize), headers = creditcard_request_header)
		
	
    def delete_creditcard(self, instant_buy_key):
	
	action_name = '/' + str(instant_buy_key)
        request_headers = {"merchantKey": str(self.merchant_key), 'Content-Type': 'application/json', 'Accept': 'application/json'}
        
        return requests.delete(self.host_uri + self.resource_name + action_name, headers=request_headers)
