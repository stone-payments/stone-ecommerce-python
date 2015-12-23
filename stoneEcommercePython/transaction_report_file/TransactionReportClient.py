import urlparse
from uuid import UUID

import requests

from stoneEcommercePython.ConfigurationUtility import ConfigurationUtility


class TransactionReport(object):
    def __init__(self, merchant_key, host_uri, configuration_utility=ConfigurationUtility()):
        self.__configuration_utility = configuration_utility
        if merchant_key is None or merchant_key == UUID('00000000-0000-0000-0000-000000000000'):
            merchant_key = self.__configuration_utility.merchant_key()
        self.merchant_key = merchant_key
        if host_uri is None:
            raise ValueError("host_uri have None value")
        self.host_uri = host_uri

    def download_report(self, file_date):
        request_header = {"MerchantKey": str(self.merchant_key)}
        resource = "/TransactionReportFile/GetStream?fileDate=" + file_date
        return requests.get(urlparse.urljoin(self.host_uri, resource), headers=request_header)

    def download_report_to_file(self, file_date, file_name):
        http_response = self.download_report(file_date)
        if http_response.status_code == requests.codes.ok:
            with open(file_name, 'w') as f:
                f.write(http_response.text)

        return http_response.status_code
