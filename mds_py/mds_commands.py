import os
import redis
from redis.commands.search.field import TextField, NumericField, TagField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.search.query import NumericFilter, Query

from . mds_vocabulary import Vocabulary as voc
import mds_py.mds_utils as utl
from cerberus import errors, Validator, SchemaError
import re
import yaml

class Commands:

    @staticmethod
    def createIndex(rs: redis.Redis, idx_name: str, mds_home: str, schema_path: str, register: bool) -> str|None:        
        try:
            sch = utl.getSchemaFromFile(schema_path)
            v = Validator()
            p_dict: dict = {}
            if v.validate(utl.doc_0, sch):
                n_doc = v.normalized(utl.doc_0, sch)
                p_dict = n_doc.get('props').items() 
            rs.ft(idx_name).create_index(utl.ft_schema(p_dict), definition=IndexDefinition(prefix=[utl.prefix(idx_name)]))
        except:
            print('Index already exists')
        finally:
            # if idx_name == voc.IDX_REG:
            Commands.registerIndex(rs, mds_home, n_doc, sch)
        return 

    def createIndices(rs: redis.Redis, mds_home:str, dir: str, fileList: list, register: bool):
        for file in fileList:
            idx_name = utl.schema_name(file)            
            path = os.path.join(mds_home, dir, file)
            Commands.createIndex(rs, idx_name, mds_home, path, True)

    @staticmethod
    def registerIndex(rs: redis.Redis, mds_home: str, n_doc:dict, sch):
        ''' Register index in dx_reg '''         
        file = os.path.join(mds_home, voc.BOOTSTRAP, voc.IDX_REG + '.yaml')
        idx_reg_dict: dict = {
            voc.NAME: n_doc.get(voc.NAME),
            voc.NAMESPACE: n_doc.get(voc.NAMESPACE),
            voc.PREFIX: n_doc.get(voc.PREFIX),
            voc.LABEL: n_doc.get(voc.LABEL),
            voc.KIND: n_doc.get(voc.KIND),
            voc.SOURCE: str(sch)
        }
        # print('IDX_REG record: {}'.format(idx_reg_dict[voc.LABEL]))
        utl.updateRecord(rs, voc.IDX_REG, voc.IDX_REG, file, idx_reg_dict)

    # def updateRecords(rs:redis.Redis, _list:list[dict]) -> str|None:
    #     pipe = rs.pipeline()
    #     try:
    #         for map in _list:
    #             pipe.hset('hash', mapping=map)
    #         pipe.execute()
    #         return voc.OK
    #     except:
    #         return None
 
    def search(rs: redis.Redis, index: str, query: str) -> str|None:
        return rs.set(index, query)

    def set(rs: redis.Redis, index: str, query: str) -> str|None:
        return rs.set(index, query)

    
