import mds_py.mds_utils as utl
from mds_py.mds_client import Client
from mds_py.mds_vocabulary import Vocabulary as voc
from cerberus import errors, Validator, SchemaError

import os
import yaml
import redis
import re

client = Client(None)
client.boot_strap()

file = client.schema_file_name(voc.BOOTSTRAP, 'idx_reg')
schema = client.schema_from_file(file)

v = Validator()
if v.validate(utl.doc_0, schema):
    n_doc = v.normalized(utl.doc_0, schema)
    p_dict = n_doc.get('props')
    
    # print(n_doc.get('props'))

    # client.create_index(voc.BOOTSTRAP, 'idx_reg')
    # client.update_record(voc.BOOTSTRAP, 'idx_reg', p_dict)

    # print(client.index_info('idx_reg'))
else:
    print(v.errors)