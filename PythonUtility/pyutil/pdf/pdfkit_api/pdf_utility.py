__author__ = 'Nejati'

from jinja2 import Template
import pdfkit


def load_template_from_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as template_file:
        return template_file.read()


def fulfill_template(template_str, data):
    template = Template(template_str)
    string_array = template.render(**data)
    return string_array


def convert_into_pdf_stream(string_array, options=None, css=None, config=None):
    if config:
        config = pdfkit.configuration(**config)
    if not options:
        options = dict()
    options.update({'quiet': ''})
    bytes_array = pdfkit.PDFKit(url_or_file=string_array, type_='string', options=options, css=css,
                                configuration=config).to_pdf()
    return bytes_array


def save_into_file(file_fullname, bytes_stream):
    with open(file_fullname, 'wb') as output:
        output.write(bytes_stream)
