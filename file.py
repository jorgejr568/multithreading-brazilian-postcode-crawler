import json
import os
import re

from formatter import FileFormatter


class AddressFile:
    BASE_PATH = os.path.dirname(os.path.abspath(__file__)) + '/addresses'

    @staticmethod
    def write(address):
        file = open(AddressFile.__path(address), 'w+')
        file.write(json.dumps(vars(address)))
        file.close()

    @staticmethod
    def exists(address):
        return os.path.exists(AddressFile.__path(address))

    @staticmethod
    def __path(address):
        return AddressFile.BASE_PATH + '/' + address.postcode + '.json'

    @staticmethod
    def list():
        addresses = []

        for r, d, f in os.walk(AddressFile.BASE_PATH):
            for file in f:
                if '.json' in file:
                    addresses.append(int(FileFormatter.remove_extension(file)))

        return addresses
