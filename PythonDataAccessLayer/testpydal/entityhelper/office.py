__author__ = 'h.rouhani'


class Office:
    def _getName(self):
        return self.name

    def _setName(self, name):
        self.name = name

    def _getCode(self):
        return self.code

    def _setCode(self, code):
        self.cod = code

    Name = property(_getName, _setName)
    Code = property(_getCode, _setCode)
