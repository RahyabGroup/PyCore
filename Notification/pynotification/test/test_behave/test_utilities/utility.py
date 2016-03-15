__author__ = 'azh'


def contains(dict, key, value):
    for row in dict:
        if row[key] == value:
            return True
    return False


# def exist_in_each_row_key_value(dict, key, value):
#     for row in dict:
#         for key in row:
#             if row[key] == value:
#                 return True
#         return False
#     return False

def exists_in_or_result(row, criteria):
    flag = False
    for query in criteria:
        if criteria[query] in row[query]:
            flag = True
            break
    return flag


def exists_in_and_result(row, criteria):
    for query in criteria:
        if criteria[query] not in row[query]:
            return False
    return True


def exists_in_each_row(row, value):
    for key in row:
        if row[key] == value:
            return True
    return False


def value_of(dict, index_key, index_value, key):
    for row in dict:
        if row[index_key] == index_value:
            return row[key]
    return 'Not Found'
