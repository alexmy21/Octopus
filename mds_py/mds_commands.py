import redis
from redis.commands.search.field import TextField, NumericField, TagField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.search.query import NumericFilter, Query

from . mds_vocabulary import Vocabulary as voc
from . mds_utils import Utils as utl
from cerberus import errors, Validator, SchemaError
import re
import yaml

class Commands:

    def createIndex(rs: redis.Redis, idx_name: str, schema_path: str) -> str|None:
        try:
            sch = utl.getSchemaFromFile(schema_path)
            v = Validator()
            k_dict: dict = {}
            if v.validate(utl.doc_0, sch):
                n_doc = v.normalized(utl.doc_0, sch)
                k_dict = n_doc.get('props').items() 

            rs.ft(idx_name).create_index(utl.ft_schema(k_dict), definition=IndexDefinition(prefix=[utl.prefix(idx_name)]))
            return voc.OK
        except:
            return 
    
    def updateRecord(rs:redis.Redis, pref: str, idx_name: str, schema_path: str, map:dict) -> str|None:
        _pref = ''
        if pref.endswith(':'): _pref = pref
        else: _pref = pref + ':'

        sch = utl.getSchemaFromFile(schema_path)        
        v = Validator()        
        k_list: dict = []
        id = ''
        if v.validate(utl.doc_0, sch):
            n_doc = v.normalized(utl.doc_0, sch)
            k_list = n_doc.get('keys')
            id = utl.sha1(k_list, map)
            map['__id'] = id
        print(map)

        return rs.hset(_pref + id, mapping=map)

    def updateRecords(rs:redis.Redis, _list:list[dict]) -> str|None:
        pipe = rs.pipeline()
        try:
            for map in _list:
                pipe.hset('hash', mapping=map)
            pipe.execute()
            return voc.OK
        except:
            return None
 
    def search(rs: redis.Redis, index: str, query: str) -> str|None:
        return rs.set(index, query)

    def set(rs: redis.Redis, index: str, query: str) -> str|None:
        return rs.set(index, query)

    
