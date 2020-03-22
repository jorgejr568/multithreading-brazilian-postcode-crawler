import requests


class AddressViaCepApi:
    ENDPOINT = 'https://viacep.com.br/ws'
    FORMAT = 'json'

    @staticmethod
    def request(postcode):
        try:
            response = requests.get(
                url=AddressViaCepApi.url(postcode),
                params={}
            )
            print(response.json())
            if response.status_code == 200 and not 'erro' in response.json():
                return response.json()

            return False

        except:
            return False

    @staticmethod
    def url(postcode):
        return AddressViaCepApi.ENDPOINT + '/' + postcode + '/' + AddressViaCepApi.FORMAT


class AddressWidenetCepApi:
    ENDPOINT = 'https://apps.widenet.com.br/busca-cep/api/cep'
    FORMAT = 'json'

    @staticmethod
    def request(postcode):
        try:
            response = requests.get(
                url=AddressWidenetCepApi.url(postcode),
                params={}
            )
            print(response.json())
            if response.status_code == 200 and response.json()['ok']:
                return response.json()

            return False

        except:
            return False

    @staticmethod
    def url(postcode):
        return AddressWidenetCepApi.ENDPOINT + '/' + postcode + '.' + AddressWidenetCepApi.FORMAT


class AddressFSOACepApi:
    ENDPOINT = 'http://fsoa.cefet-rj.local/cep-api.php'

    @staticmethod
    def request(postcode):
        try:
            response = requests.get(
                url=AddressFSOACepApi.ENDPOINT,
                params={
                    "cep": postcode
                }
            )
            print(response.content)
            if response.status_code == 200 and 'error' not in response.json():
                return response.json()

            return False

        except:
            return False
