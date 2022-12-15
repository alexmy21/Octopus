
from typing import Sequence
from . mds_vocabulary import Vocabulary as voc

import yaml
import redis
import hashlib

from redis.commands.search.field import TextField, NumericField, TagField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.search.query import NumericFilter, Query


class Utils:

    doc_0 = {   
        'props': {}
    }

    def schemaFile(schema: str) -> str|None:
        return schema + '.yaml' 

    def prefix(idx_name: str) -> str:
        return idx_name + ':'

    def getConfig(file_name: str|None) -> dict|None:
        config: dict | None
        try:
            with open(file_name, 'r') as file:
                config = yaml.safe_load(file)
        except:
            raise RuntimeError(f"Error: Problem with '{file_name}' file.")            
        return config

    def getRedis(config: dict) -> redis.Redis|None:
        host = config.get(voc.REDIS, {}).get(voc.REDIS_HOST)
        port = config.get(voc.REDIS, {}).get(voc.REDIS_PORT)

        return redis.StrictRedis(host, port)

    # def getSubDict(self, dict, key) ->  dict:
    #     new_dict = {}
        
    #     for key, value in dict[key].items():
    #         if type(value) == dict:
    #             print(key)
    #             self.getSubDict(value)
    #         else:
    #             new_dict[key] = value
    #     return new_dict

    def getSchemaFromFile(file_name):       
        with open(file_name, 'r') as file:
            return yaml.safe_load(file)

    def ft_schema(schema: dict) -> tuple|None:
        dictlist = []
        tmp: str
        for key, value in schema:
            if value == 'tag':
                temp = TagField(key)
                dictlist.append(temp)
            elif value == 'numeric':
                temp = NumericField(key)
                dictlist.append(temp)
            else:
                temp = TextField(key)
                dictlist.append(temp)            
            
        return tuple(i for i in dictlist)

    # Generates SHA1 hash code from key fields of props 
    # dictionary
    def sha1(keys: list, props: dict) -> str|None:
        sha = '' 
        for key in keys:
            sha+= props.get(key)

        m = hashlib.sha1()
        m.update(sha.encode())
        return m.hexdigest()