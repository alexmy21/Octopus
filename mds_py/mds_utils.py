
from mds_vocabulary import Vocabulary as voc

import yaml
import redis

class Utils:

    def getConfig(file_name: str | None) -> dict|None:
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

    def getSubDict(self, dict, key) ->  dict:
        new_dict = {}
        
        for key, value in dict[key].items():
            if type(value) == dict:
                print(key)
                self.getSubDict(value)
            else:
                new_dict[key] = value

        return new_dict

    def getSchemaFromFile(file_name):       
        with open(file_name, 'r') as file:
            schema = yaml.safe_load(file)        

        return schema

    def updateRecord(mds:redis.Redis, map:dict) -> str|None:
        ret: str|None
        for key, value in map.items():
            ret = mds.hset('hash', key, value)

        return ret