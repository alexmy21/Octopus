import os
import redis as redis_server
from typing import Union

from mds_utils import Utils as utl
from mds_vocabulary import Vocabulary as voc

# from commands import Commands as cmd
# from mds_service import Service

class Client:   
    mds_home: Union[str, None]
    boot:str
    config: str
    schemas:str
    processors:str    

    def __init__(self, _mds_home: Union[str, None] = None ):
        if _mds_home is not None:
            if _mds_home in os.environ:
                self.mds_home = os.environ.get(_mds_home) 
            elif os.path.exists(_mds_home):
                self.mds_home = _mds_home
            else:
                self.mds_home = None
                raise RuntimeError(f"Error: Provided '{_mds_home}' mds home directory doesn't exist.")
        
        elif voc.MDS_HOME in os.environ:
                self.mds_home = os.environ.get(voc.MDS_HOME)
        else:
            self.mds_home = None
            raise RuntimeError(f"Error: Provided '{_mds_home}' mds home directory doesn't exist.")

    def redis(self):
        return redis_server.StrictRedis()
    
    def bootstrap(self):
        path = os.path.join(self.mds_home, voc.CONFIG, voc.CONFIG_FILE) 
        print(path) 

        config = utl.getConfig(path) 
        print(config)  

        r_server:redis_server = utl.getRedis(config) 
   
client = Client( )
print(client.mds_home)

client.bootstrap()
