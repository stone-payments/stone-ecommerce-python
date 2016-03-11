import requests
import json
from AbstractResource import AbstractResource
from uuid import UUID
from data_contracts import buyer


class uuid_serialize(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
          return str(obj)
            # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)
		

class BuyerResource(AbstractResource):

    def __init__(self, merchant_key=None, environment=None, http_content_type=None, host_uri=None):
        super(BuyerResource, self).__init__(merchant_key, environment, http_content_type, "/Buyer", host_uri)

    def get_buyer(self, buyer_key):
        action_name = '/' + str(buyer_key)
        request_headers = {"merchantKey": str(self.merchant_key), 'Content-Type': 'application/json', 'Accept': 'application/json'}
        
        return requests.get(self.host_uri + self.resource_name + action_name, headers=request_headers)

    def create_buyer(self, buyer_request):
        request_headers = {"MerchantKey": str(self.merchant_key), 'Content-Type': 'application/json', 'Accept': 'application/json'}

        return requests.post(self.host_uri + self.resource_name, data = json.dumps(buyer_request, cls=uuid_serialize), headers = request_headers)
