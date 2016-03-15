__author__ = 'h.rouhani'


class Address:
    def _setStreet(self, street):
        self.street = street

    def _getStreet(self):
        return self.street

    def _getEmail(self):
        return self.email

    def _setEmail(self, email):
        self.email = email

    Street = property(_getStreet, _setStreet)
    Email = property(_getEmail, _setEmail)

    @staticmethod
    def _getAddressInstance():
        address = Address()
        address.Street = "Pasdaran Golestan dovom"
        address.Email = "Hooman.fr@gmail.com"
        address.WebAddress = "www.fanted.com"
        return address