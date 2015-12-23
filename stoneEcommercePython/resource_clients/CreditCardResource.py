import requests

from AbstractResource import AbstractResource


class CreditCardResource(AbstractResource):

    def __init__(self, merchant_key=None, environment=None, http_content_type=None, host_uri=None):
        super(CreditCardResource, self).__init__(merchant_key, environment, http_content_type, "/CreditCard", host_uri)

    def __get_instant_buy_data_implementation(self, key, identifier_name):
        if identifier_name:
            identifier_name = '/' + identifier_name

        action_name = '/{0}{1}'.format(str(key), identifier_name)
        request_headers = {"merchantKey": str(self.merchant_key), 'Content-Type': 'application/json', 'Accept': 'application/json'}

        return requests.get(self.host_uri + self.resource_name + action_name, headers=request_headers)

    def get_instant_buy_data(self, instant_bur_key):
        return self.__get_instant_buy_data_implementation(instant_bur_key, '')

    def get_instant_buy_data_with_buyer_key(self, buyer_key):
        return self.__get_instant_buy_data_implementation(buyer_key, 'BuyerKey')

