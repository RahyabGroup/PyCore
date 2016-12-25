from pyutil.pdf.farsi_text import FarsiText

__author__ = 'root'


class FormatText:

    @staticmethod
    def get_farsi_formatted_text(text):
        return '<font>%s</font>' % FarsiText.get_farsi_text(text)
