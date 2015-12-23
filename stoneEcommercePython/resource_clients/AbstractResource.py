from abc import ABCMeta

from stoneEcommercePython.ConfigurationUtility import ConfigurationUtility
from enum_types import PlatformEnvironment


class AbstractResource(object):
    __metaclass__ = ABCMeta

    def __init__(self, merchant_key=None, environment=None, http_content_type=None, resource_name=None, host_uri=None,
                 configuration_utility=ConfigurationUtility()):
        self.__configuration_utility = configuration_utility
        if merchant_key is None:
            merchant_key = self.__configuration_utility.merchant_key()

        self.merchant_key = merchant_key
        self.plataform_environment = environment
        self.http_content_type = http_content_type

        if host_uri is not None:
            self.host_uri = host_uri
        else:
            self.host_uri = self.get_service_uri(environment)

        self.resource_name = resource_name

    def get_service_uri(self, environment):
        switch_uri = {PlatformEnvironment.production: self.__configuration_utility.production_host_uri(),
                      PlatformEnvironment.sandbox: self.__configuration_utility.sandbox_host_uri()}

        return switch_uri.get(environment)

