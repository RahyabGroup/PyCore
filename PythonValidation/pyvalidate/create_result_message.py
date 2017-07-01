__author__ = 'R.Azh'


def create_result_message(error_message, field_name, value):
    result_message = {}
    if isinstance(error_message, dict):
        result_message = error_message
    elif isinstance(error_message, str):
        result_message = {'title': error_message}
    if field_name:
        result_message['field_name'] = field_name
    result_message['value'] = value
    return result_message

