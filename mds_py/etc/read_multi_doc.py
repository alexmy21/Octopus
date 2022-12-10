# import file
import yaml
import redis

from cerberus import errors, Validator, SchemaError
import re

def getSubDict(dict, key) ->  dict:
    new_dict = {}
    for key, value in dict[key].items():
        if type(value) == dict:
            print(key)
            getSubDict(value)
        else:
            new_dict[key] = value

    return new_dict

mds = redis.StrictRedis(host='localhost', port=6379)

with open('/home/alexmy/REDIS_CLUSTER/octopus/mds_py/.mds_py/bootstrap/idx_reg.yaml', 'r') as file:
    schema = yaml.safe_load(file)

v = Validator()

doc = {
    'keys':{
        'name':'John',
        'label': 'COLUMN'
    },
    'props': {'commit_id': 'commit_id', 'source': 'json'}
}

if v.validate(doc, schema):
    n_doc = v.normalized(doc, schema)

    k_dict = getSubDict(n_doc, 'keys')
    for key, value in k_dict.items():
        mds.hset('hash', key, value)

    p_dict = getSubDict(n_doc, 'props')
    for key, value in p_dict.items():
        mds.hset('hash', key, value)
    
    # print(n_doc)
    # print(n_doc.get('keys'))
    # print(n_doc.get('props'))
else:
    print(v.errors)