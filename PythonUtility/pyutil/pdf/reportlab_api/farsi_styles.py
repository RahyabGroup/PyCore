from reportlab.lib import colors
from reportlab.platypus import TableStyle

__author__ = 'root'


class FarsiStyles:

    @staticmethod
    def get_paragraph_styles():
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT, TA_CENTER
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont

        pdfmetrics.registerFont(TTFont('Persian', 'Bahij-Nazanin-Regular.ttf'))
        pdfmetrics.registerFont(TTFont('Persian-Bold', 'Bahij-Nazanin-Bold.ttf'))
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY, fontName='Persian', fontSize=10, wordWrap='CJK'))
        styles.add(ParagraphStyle(name='Justify-Bold', alignment=TA_JUSTIFY, fontName='Persian-Bold', fontSize=10, wordWrap='CJK'))
        styles.add(ParagraphStyle(name='Right-indented', alignment=TA_RIGHT, fontName='Persian', fontSize=10,
                                  rightIndent=10, wordWrap='CJK'))
        styles.add(ParagraphStyle(name='Right', alignment=TA_RIGHT, fontName='Persian', fontSize=10,
                                  rightIndent=10, wordWrap='CJK'))
        styles.add(ParagraphStyle(name='Right-with-space', alignment=TA_RIGHT, fontName='Persian', fontSize=10,
                                  rightIndent=10, wordWrap='CJK', spaceBefore=12, spaceAfter=12, bulletAnchor='end',
                                  bulletIndent=5))
        styles.add(ParagraphStyle(name='Right-Bold', alignment=TA_RIGHT, fontName='Persian-Bold', fontSize=10, wordWrap='CJK'))
        styles.add(ParagraphStyle(name='Right-Bold-Titr', alignment=TA_RIGHT, fontName='Persian-Bold', fontSize=12,
                                  textColor=colors.cornflowerblue, wordWrap='CJK'))
        styles.add(ParagraphStyle(name='Right-small', alignment=TA_RIGHT, fontName='Persian', fontSize=8,
                                  rightIndent=20,
                                  wordWrap='CJK'))
        styles.add(ParagraphStyle(name='Centre', alignment=TA_CENTER, fontName='Persian', fontSize=10, wordWrap='CJK'))
        styles.add(ParagraphStyle(name='Centre-Bold', alignment=TA_CENTER, fontName='Persian-Bold', fontSize=10, wordWrap='CJK'))
        return styles

    @staticmethod
    def get_table_styles():
        styles = {'simple_right': TableStyle([('BACKGROUND', (0, 0), (-1, -1), colors.white),
                                              ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
                                              ('HALIGN', (0, 0), (-1, -1), 'RIGHT'),
                                              ('VALIGN', (0, 0), (0, -1), 'CENTER')]),
                  'image_info': TableStyle([('BACKGROUND', (0, 0), (-1, -1), colors.white),
                                            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
                                            ('VALIGN', (0, 1), (-1, -1), 'CENTER'),
                                            ('ALIGN', (0, 0), (0, 0), 'RIGHT'),
                                            ('ALIGN', (-1, -1), (-1, -1), 'CENTER')]),
                  'simple_right_bordered': TableStyle([('BACKGROUND', (0, 0), (-1, -1), colors.white),
                                                       ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
                                                       ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
                                                       ('LINEABOVE', (0, 0), (-1, -1),  0.25, colors.black),
                                                       ('LINEBELOW', (0, 0), (-1, -1),  0.25, colors.black),
                                                       ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                                                       ('BOX', (0, 0), (-1, -1), 0.25, colors.black)])
                  }
        return styles
