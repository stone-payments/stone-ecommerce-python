# -*- coding: utf-8 -*-
import json
import urlparse
from uuid import UUID

import requests
from data_contracts import create_sale_request, sale_options, manage_sale_request, retry_sale_request

from AbstractResource import AbstractResource


class uuid_serialize(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return str(obj)
            # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)


class SaleResource(AbstractResource):
    def __init__(self, merchant_key=None, environment=None, http_content_type=None, host_uri=None):
        super(SaleResource, self).__init__(merchant_key, environment, http_content_type, "/Sale", host_uri)

    def create_with_request(self, create_sale_request):
        request_header = {"MerchantKey": str(self.merchant_key), 'Content-Type': 'application/json',
                          'Accept': 'application/json'}
        return requests.post(urlparse.urljoin(self.host_uri, 'Sale'),
                             data=json.dumps(create_sale_request, cls=uuid_serialize), headers=request_header)

    def create_with_creditcard_collection(self, creditcard_transaction_collection):
        request = create_sale_request(creditcard_transaction_collection=creditcard_transaction_collection)
        # Se não for informado o comprador nem o carrinho de compras não será possível utilizar o serviço de anti fraude
        request['Options'] = sale_options(is_anti_fraud_enabled=False)

        return self.create_with_request(request)

    def create_with_creditcard(self, creditcard_transaction):
        creditcard_transaction_collection = [creditcard_transaction]
        return self.create_with_creditcard_collection(creditcard_transaction_collection)

    def create_with_boleto_collection(self, boleto_transaction_collection):
        request = create_sale_request(boleto_transaction_collection=boleto_transaction_collection)
        # Se não for informado o comprador nem o carrinho de compras não será possível utilizar o serviço de anti fraude
        request['Options'] = sale_options(is_anti_fraud_enabled=False)

        return self.create_with_request(request)

    def create_with_boleto(self, boleto_transaction):
        boleto_transaction_collection = [boleto_transaction]
        return self.create_with_boleto_collection(boleto_transaction_collection)

    def manage_with_request(self, manage_operation, manage_sale_request):
        # Configura o action que será utilizado
        action_name = self.resource_name + '/' + manage_operation.name

        request_header = {"MerchantKey": str(self.merchant_key), 'Content-Type': 'application/json',
                          'Accept': 'application/json'}

        return requests.post(urlparse.urljoin(self.host_uri, action_name),
                             data=json.dumps(manage_sale_request, cls=uuid_serialize), headers=request_header)

    def manage_with_order_key(self, manage_operation, order_key):
        request = manage_sale_request(order_key=order_key)
        return self.manage_with_request(manage_operation, request)

    def manage_with_creditcard_collection(self, manage_operation, order_key, manage_creditcard_transaction_collection):
        request = manage_sale_request(order_key=order_key,
                                      manage_creditcard_transaction_collection=manage_creditcard_transaction_collection)
        return self.manage_with_request(manage_operation, request)

    def manage_with_creditcard(self, manage_operation, order_key, manage_creditcard_transaction):
        manage_creditcard_transaction_collection = [manage_creditcard_transaction]
        return self.manage_with_creditcard_collection(manage_operation, order_key,
                                                      manage_creditcard_transaction_collection)

    def retry_with_request(self, retry_sale_request):
        request_header = {"MerchantKey": str(self.merchant_key), 'Content-Type': 'application/json',
                          'Accept': 'application/json'}
        action_name = self.resource_name + '/Retry'
        return requests.post(urlparse.urljoin(self.host_uri, action_name),
                             data=json.dumps(retry_sale_request, cls=uuid_serialize), headers=request_header)

    def retry_with_order_key(self, order_key):
        request = retry_sale_request(order_key=order_key)
        return self.retry_with_request(request)

    def retry_with_creditcard_collection(self, order_key, retry_sale_creditcard_transaction_collection):
        request = retry_sale_request(order_key=order_key,
                                     retry_sale_creditcard_transaction_collection=retry_sale_creditcard_transaction_collection)
        return self.retry_with_request(request)

    def retry_with_creditcard(self, order_key, retry_sale_creditcard_transaction):
        retry_sale_creditcard_transaction_collection = [retry_sale_creditcard_transaction]
        return self.retry_with_creditcard_collection(order_key, retry_sale_creditcard_transaction_collection)

    def query_order_with_key(self, order_key):
        return self.__query_implementation('OrderKey', str(order_key))

    def query_order_with_reference(self, order_reference):
        return self.__query_implementation('OrderReference', order_reference)

    def query_creditcard_transaction_with_key(self, creditcard_transaction_key):
        return self.__query_implementation('CreditCardTransactionKey', str(creditcard_transaction_key))

    def query_creditcard_transation_with_reference(self, creditcard_transaction_reference):
        return self.__query_implementation('CreditCardTransactionReference', creditcard_transaction_reference)

    def query_boleto_transaction_with_key(self, boleto_transaction_key):
        return self.__query_implementation('BoletoTransactionKey', boleto_transaction_key)

    def query_boleto_transation_with_reference(self, boleto_transaction_reference):
        return self.__query_implementation('BoletoTransactionReference', boleto_transaction_reference)

    def __query_implementation(self, identifier_name, value):
        action_name = 'Sale/Query/{0}={1}'.format(identifier_name, value)

        request_header = {"MerchantKey": str(self.merchant_key), 'Content-Type': 'application/json',
                          'Accept': 'application/json'}
        return requests.get(urlparse.urljoin(self.host_uri, action_name), headers=request_header)
