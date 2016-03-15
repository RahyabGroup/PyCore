from datetime import datetime

__author__ = 'azh'

#
# def read_image_file(file_path):
#     open(file_path, 'rb')
#
#     return


def generate_simple_unique_int():
    dt = datetime.now()
    unique_int = dt.year + dt.month + dt.day + dt.hour + dt.minute + dt.second + dt.microsecond
    return unique_int

# uuid.uuid1().int