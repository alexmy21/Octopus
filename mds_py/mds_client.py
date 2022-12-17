import os
import redis as srv

import mds_py.mds_utils as utl
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
        
        path = os.path.join(self.mds_home, voc.CONFIG, utl.idxFileWithExt(voc.CONFIG_FILE)) 
        self.config = utl.getConfig(path) 

    # Following is a list  wrappers for commands from Commands module
    #====================================================================
    def schema_file_name(self, schema_dir: str, schema_name: str) -> str|None:
        return os.path.join(self.mds_home, schema_dir, utl.idxFileWithExt(schema_name))

    def schema_from_file(self, file_name: str) -> str|None:
        return utl.getSchemaFromFile(file_name)

    def index_info(self, idx_name: str) -> str|None:
        rs = utl.getRedis(self.config)
        return rs.ft(idx_name).info()

    def create_index(self, schema_dir: str, schema_name: str) -> str|None :
        rs = utl.getRedis(self.config)
        schema_path = os.path.join(self.mds_home, schema_dir, utl.idxFileWithExt(schema_name))
        ret_str = cmd.createIndex(rs, schema_name, self.mds_home, schema_path)

        return ret_str
    
    def update_record(self, schema_dir: str, schema_name: str, map: dict) -> str|None:
        rs = utl.getRedis(self.config)
        path = os.path.join(self.mds_home, schema_dir, utl.idxFileWithExt(schema_name))
        # rs:redis.Redis, pref: str, idx_name: str, schema_path: str, map:dict
        return utl.updateRecord(rs, schema_name, schema_name, path, map)

    def search(self, idx: str):
        rs = utl.getRedis(self.config)
        return rs.ft(idx)    

    def boot_strap(self):
        rs = utl.getRedis(self.config)
        '''First create idx_reg index'''
        schema_path = os.path.join(self.mds_home, voc.BOOTSTRAP, utl.idxFileWithExt(voc.IDX_REG))
        cmd.createIndex(rs, voc.IDX_REG, self.mds_home, schema_path, False)
        '''
        get idx files from bootstrap directory
        and register them in idx_reg index
        all including idx_rg index itself 
        '''
        fileList = utl.fileList(self.boot)
        print('File List: \n {}'.format(fileList))

        # rs: redis.Redis, mds_home:str, dir: str, fileList: list, register: bool
        cmd.createIndices(rs, self.mds_home, self.boot, fileList, True)
       
    print('=================== Client new instance =============================')