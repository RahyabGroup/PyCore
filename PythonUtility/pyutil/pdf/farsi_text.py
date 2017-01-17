__author__ = 'root'
from rtl import reshaper
from bidi.algorithm import get_display


class FarsiText:
    @staticmethod
    def get_farsi_text(text):
        if reshaper.has_arabic_letters(text):
            words = text.split()
            reshaped_words = []
            for word in words:
                if reshaper.has_arabic_letters(word):
                    reshaped_text = reshaper.reshape(word)
                    bidi_text = get_display(reshaped_text)
                    reshaped_words.append(bidi_text)
                else:
                    reshaped_words.append(word)
            reshaped_words.reverse()
            return ' '.join(reshaped_words)
        return text

    @staticmethod
    def get_farsi_numbers(text):
        return reshaper.replace_digits(text)

    @staticmethod
    def get_jalali_date_from_isoformat_date(isoformat_date):
        import dateutil.parser
        import jalaali

        _date = dateutil.parser.parse(isoformat_date)
        jalai_date = jalaali.Jalaali().to_jalaali(_date.year, _date.month, _date.day)
        return reshaper.replace_digits('{}-{}-{}'.format(jalai_date['jy'], jalai_date['jm'], jalai_date['jd']))

    @staticmethod
    def get_reversed_text(text):
        if reshaper.has_arabic_letters(text):
            words = text.split()
            reshaped_words = []
            for word in words:
                    reshaped_words.append(word)
            reshaped_words.reverse()
            return ' '.join(reshaped_words)
        return text
