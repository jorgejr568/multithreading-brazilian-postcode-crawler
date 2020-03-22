from formatter import PostcodeFormatter


class Address:
    def __init__(self, postcode, state, city, neighborhood, street):
        self.postcode = postcode
        self.state = state
        self.city = city
        self.neighborhood = neighborhood
        self.street = street


class AddressFactory:
    @staticmethod
    def from_viacep_json(json):
        return Address(PostcodeFormatter.postcode(json['cep']), json['uf'], json['localidade'], json['bairro'], json['logradouro'])

    @staticmethod
    def from_widenet_json(json):
        return Address(PostcodeFormatter.postcode(json['code']), json['state'], json['city'], json['district'], json['address'])

    @staticmethod
    def from_fsoa_json(json):
        return Address(PostcodeFormatter.postcode(json['code']), json['state'], json['city'], json['district'], json['street'])
