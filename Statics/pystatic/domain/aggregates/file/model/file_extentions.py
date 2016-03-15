import itertools

__author__ = 'root'


class FileExtentions:
    _IMAGE_EXTENTIONS = ['png', 'jpg', 'jpeg', 'gif']
    _VIDEO_EXTENTIONS = ['flv', 'avi', 'mpg', 'mpeg', '3gp', 'mkv']

    FILE_EXTENTIONS = list(itertools.chain(_VIDEO_EXTENTIONS, _IMAGE_EXTENTIONS))
