__author__ = 'azh'


def contains(dict, key, value):
    for row in dict:
        if row[key] == value:
            return True
    return False


def value_of(dict, index_key, index_value, key):
    for row in dict:
        if row[index_key] == index_value:
            return row[key]
    return 'Not Found'
