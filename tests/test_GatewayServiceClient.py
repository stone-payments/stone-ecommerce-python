from uuid import UUID

from stoneEcommercePython import GatewayServiceClient
from data_contracts import create_creditcard_request, billing_address
import enum_types
import pytest


def test_create_gateway_service_client():
    try:
        merchant_key = UUID('85328786-8BA6-420F-9948-5352F5A183EB')
        end_point = "https://transaction.stone.com.br"
        billing_address_data = billing_address(
                                country='Brazil',
                                state='RJ',
                                city='Tatooine',
                                district='Mos Eisley',
                                street='Mos Eisley Cantina',
                                number='123',
                                complement='',
                                zip_code='20001000')

        credit_card_request_data = create_creditcard_request(
                                billing_address=billing_address_data,
                                creditcard_brand='Visa',
                                creditcard_number='4111111111111111',
                                exp_month='10',
                                exp_year='22',
                                holder_name='LUKE SKYWALKER',
                                is_one_dollar_auth_enbacled='false')

        service_client = GatewayServiceClient(
                                merchant_key,
                                enum_types.PlatformEnvironment.sandbox,
                                enum_types.HttpContentTypeEnum.json,
                                end_point)
    except Exception as ex:
        pytest.fail(ex.message)
