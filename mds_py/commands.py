# from client import Client as mds
# from cerberus import errors, Validator, SchemaError
import re
import yaml
import redis

class Commands:
    mds_home:str

    def __init__(self, _mds_home):        
        self.mds_home = _mds_home

    def getCmdId(self):
        return self.id

    
