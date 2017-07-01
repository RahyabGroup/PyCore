import textwrap
from pyutil.pdf.farsi_text import FarsiText

__author__ = 'R.Azh'


class FormatText:

    @staticmethod
    def get_farsi_formatted_text(text, wrap_length=None):
        farsi_text = FarsiText.get_farsi_text(text)
        if wrap_length:
            line_list = textwrap.wrap(farsi_text, wrap_length)
            line_list.reverse()
            farsi_text = '<br/>'.join(line_list)
        return '<font>%s</font>' % farsi_text

    @staticmethod
    def get_farsi_bulleted_text(text, wrap_length=None):
        farsi_text = FarsiText.get_farsi_text(text)
        if wrap_length:
            line_list = textwrap.wrap(farsi_text, wrap_length)
            line_list.reverse()
            line_list[0] = '{} &#x02022;'.format(line_list[0])
            farsi_text = '<br/>'.join(line_list)
            return '<font>%s</font>' % farsi_text
        return '<font>%s &#x02022;</font>' % farsi_text
