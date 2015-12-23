import json
import os


class ConfigurationUtility(object):
    def __init__(self, configuration=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config.json')):
        if os.path.exists(configuration):
            with open(configuration, 'r') as config:
                self.__configuration = json.load(config)
        else:
            self.__configuration = {}

    def merchant_key(self):
        return self.__configuration.get('merchant_key')

    def production_host_uri(self):
        return self.__configuration.get('production_host_uri')

    def sandbox_host_uri(self):
        return self.__configuration.get('sandbox_host_uri')
