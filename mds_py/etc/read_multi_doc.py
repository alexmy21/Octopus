# import file
import yaml
import redis

from cerberus import errors, Validator, SchemaError
import re

def getSubDict(dict: dict, key: str) ->  dict:
    new_dict = {}
    if dict[key] is not None:
        for key, value in dict[key].items():
            if type(value) == dict:
                print(key)
                getSubDict(value)
            else:
                new_dict[key] = value

    return new_dict

mds = redis.StrictRedis(host='localhost', port=6379)

with open('/home/alexmy/PYTHON/Octopus/mds_py/.mds_py/bootstrap/proc_reg.yaml', 'r') as file:
    schema = yaml.safe_load(file)

v = Validator()

doc = {
    'keys':{
        'name':'John',
        'label': 'COLUMN'
    },
    'props': {}
}

if v.validate(doc, schema):
    n_doc = v.normalized(doc, schema)

    k_dict = getSubDict(n_doc, 'keys')
    for key, value in k_dict.items():
        mds.hset('hash', key, value)

    p_dict: dict|None = getSubDict(n_doc, 'props')

    if p_dict is not None:
        for key, value in p_dict.items():
            mds.hset('hash', key, value)
    
    print(n_doc)
    print(n_doc.get('keys'))
    print(n_doc.get('props'))
else:
    print(v.errors)