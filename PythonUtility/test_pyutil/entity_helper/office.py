__author__ = 'h.rouhani'


class Office:
    def _getName(self):
        return self.nameAttr

    def _setName(self, name):
        self.nameAttr = name

    def _getCode(self):
        return self.codeAttr

    def _setCode(self, code):
        self.codeAttr = code

    Name = property(_getName, _setName)
    Code = property(_getCode, _setCode)
