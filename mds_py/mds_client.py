import os
import redis as srv

from . mds_utils import Utils as utl
from . mds_vocabulary import Vocabulary as voc

from . mds_commands import Commands as cmd

class Client:   
    mds_home: str|None
    boot:str
    config: str
    schemas:str
    processors:str 

    def __init__(self, _mds_home: str|None = None ):
        if _mds_home is not None:
            if _mds_home in os.environ:
                self.mds_home = os.environ.get(_mds_home) 
            elif os.path.exists(_mds_home):
                self.mds_home = _mds_home
            else:
                self.mds_home = None
                raise RuntimeError(f"Error: Provided '{_mds_home}' mds home directory doesn't exist.")        
        elif voc.MDS_PY in os.environ:
                self.mds_home = os.environ.get(voc.MDS_PY)
        else:
            self.mds_home = None
            raise RuntimeError(f"Error: Provided '{_mds_home}' mds home directory doesn't exist.")

         # set path for all standard directories in mds_home
        self.boot = os.path.join(self.mds_home, voc.BOOTSTRAP)
        self.schemas = os.path.join(self.mds_home, voc.SCHEMAS)
        self.processors = os.path.join(self.mds_home, voc.PROCESSORS)
        path = os.path.join(self.mds_home, voc.CONFIG, voc.CONFIG_FILE) 
        self.config = utl.getConfig(path) 

    # Following is a list  wrappers for commands from Commands module
    #====================================================================
    def create_index(self, schema_name: str) -> str|None :
        rs = utl.getRedis(self.config)
        path = os.path.join(self.mds_home, voc.SCHEMAS, utl.schemaFile(schema_name))
        return cmd.createIndex(rs, schema_name, path)
    
    def create_core_index(self, schema_name: str) -> str|None :
        rs = utl.getRedis(self.config)
        path = os.path.join(self.mds_home, voc.BOOTSTRAP, utl.schemaFile(schema_name))
        return cmd.createIndex(rs, schema_name, path)
    
    def update_record(self, schema_name: str, map: dict) -> str|None:
        rs = utl.getRedis(self.config)
        path = os.path.join(self.mds_home, voc.SCHEMAS, utl.schemaFile(schema_name))
        # rs:redis.Redis, pref: str, idx_name: str, schema_path: str, map:dict
        return cmd.updateRecord(rs, schema_name, schema_name, path, map)

    def update_core_record(self, schema_name: str, map: dict) -> str|None:
        rs = utl.getRedis(self.config)
        path = os.path.join(self.mds_home, voc.BOOTSTRAP, utl.schemaFile(schema_name))
        # rs:redis.Redis, pref: str, idx_name: str, schema_path: str, map:dict
        return cmd.updateRecord(rs, schema_name, schema_name, path, map)

    def set(self, key: str, val: str) -> str:
        rs = utl.getRedis(self.config)
        return cmd.set(rs, key, val)
    
    def search(self, idx: str):
        rs = utl.getRedis(self.config)
        return self.redis().ft(idx)
