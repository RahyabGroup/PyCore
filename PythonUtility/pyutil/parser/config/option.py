__author__ = 'H.Rouhani'


class Option:
    _option_name = None
    _section = None

    def __init__(self, option_name, section):
        self._section = section
        self._option_name = option_name

    def string_get(self):
        option_value = self._section._cfg._parser.get(self._section._section_name, self._option_name)
        if option_value.strip().lower() == "none":
            return None
        return option_value

    def int_get(self):
        if self.string_get():
            return self._section._cfg._parser.getint(self._section._section_name, self._option_name)

    def bool_get(self):
        if self.string_get():
            return self._section._cfg._parser.getint(self._section._section_name, self._option_name)

    def float_get(self):
        if self.string_get():
            return self._section._cfg._parser.getfloat[float](self._section._section_name, self._option_name)

    def set(self, value):
        self._section._cfg._parser.set(self._section._section_name, self._option_name, value)
        with open(self._section._cfg._file_path, 'w') as conf_file:
            self._section._cfg._parser.write(conf_file)
