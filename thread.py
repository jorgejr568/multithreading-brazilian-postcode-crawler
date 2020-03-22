import _thread

from address import AddressFactory
from api import AddressViaCepApi, AddressWidenetCepApi, AddressFSOACepApi
from file import AddressFile


class AddressViaCepCrawlerThread:
    @staticmethod
    def run(postcode):
        result = AddressViaCepApi.request(postcode)
        if result:
            address = AddressFactory.from_viacep_json(result)
            AddressFile.write(address)

            print(postcode, ' - Worked - ', result)
        else:
            print(postcode, ' - Error')


class AddressViaCepCrawlerThreadFactory:
    @staticmethod
    def run(postcode):
        print('AddressViaCepCrawlerThread added ', postcode)
        return _thread.start_new_thread(AddressViaCepCrawlerThread.run, (postcode,))


class AddressWidenetCrawlerThread:
    @staticmethod
    def run(postcode):
        result = AddressWidenetCepApi.request(postcode)
        if result:
            address = AddressFactory.from_widenet_json(result)
            AddressFile.write(address)

            print(postcode, ' - Worked - ', result)
        else:
            print(postcode, ' - Error')


class AddressWidenetCrawlerThreadFactory:
    @staticmethod
    def run(postcode):
        print('AddressWidenetCrawlerThread added - ', postcode)
        return _thread.start_new_thread(AddressWidenetCrawlerThread.run, (postcode,))


class AddressFSOACrawlerThread:
    @staticmethod
    def run(postcode):
        result = AddressFSOACepApi.request(postcode)
        if result:
            address = AddressFactory.from_fsoa_json(result)
            AddressFile.write(address)

            print(postcode, ' - Worked - ', result)
        else:
            print(postcode, ' - Error')


class AddressFSOACrawlerThreadFactory:
    @staticmethod
    def run(postcode):
        print('AddressFSOACrawlerThread added - ', postcode)
        return _thread.start_new_thread(AddressFSOACrawlerThread.run, (postcode,))
