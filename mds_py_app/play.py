import os
from mds_py.mds_utils import Utils as utl
from mds_py.mds_client import Client as clnt
from mds_py.mds_vocabulary import Vocabulary as voc

import yaml
import redis

from cerberus import errors, Validator, SchemaError
import re

def getSubDict(map: dict, key: str):
    new_dict = {}
    if map[key] is not None:
        for key, value in map[key].items():
            if type(value) == dict:
                print(key)
                getSubDict(value)
            else:
                new_dict[key] = value

    return new_dict

mds = redis.StrictRedis(host='localhost', port=6379)

client = clnt(None)

mds_home = client.mds_home
boot = client.boot
file = os.path.join(boot, 'idx_reg.yaml')
schema = utl.getSchemaFromFile(file)

v = Validator()

if v.validate(utl.doc_0, schema):
    n_doc = v.normalized(utl.doc_0, schema)
    p_dict = n_doc.get('props')
    # utl.updateRecords(mds, seq)
    print(n_doc.get('props'))
else:
    print(v.errors)

client.create_index(voc.BOOTSTRAP, 'idx_reg')
client.update_record(voc.BOOTSTRAP, 'idx_reg', p_dict)

rs = utl.getRedis(client.config)
print(rs.ft('idx_reg').info())