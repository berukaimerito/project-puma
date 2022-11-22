import ast



def str_to_dict(str):
    return ast.literal_eval((str))


import json
def str_to_json(str):
    return json.loads(str)

# def list_str_to_json(list):
#     return json.dumps(list)


def get_id(user):
    return user['_id']['$oid']

