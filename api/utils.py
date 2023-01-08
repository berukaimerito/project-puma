import ast



def scripts_to_dict(lst):
    output = []
    for key_value in lst:
        key, value = key_value.split(': ', 1)
        if not output or key in output[-1]:
            output.append({})
        output[-1][key] = value



def str_to_dict(string):
    data = json.loads(string)
    return data

import json
def str_to_json(str):
    return json.loads(str)

# def list_str_to_json(list):
#     return json.dumps(list)


def get_id(user):
    return user['_id']['$oid']

