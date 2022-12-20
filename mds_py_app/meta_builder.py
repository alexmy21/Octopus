import os
import pathlib
from mds_py.mds_client import Client
from mds_py.mds_vocabulary import Vocabulary as voc
from pathlib import Path

FILE = 'file'

client = Client()
client.bootstrap()

schema = client.schema_file_name(voc.SCHEMAS, FILE)
print(voc.SCHEMAS)
client.create_index(voc.SCHEMAS, FILE)

def fileMeta(client: Client, file: str, schema: str) -> str|None:
    stats = os.stat(file)
    map = {
        voc.NAME: f'{file}',
        voc.LABEL: 'FILE',
        'item_prefix': 'file',
        'file_type': pathlib.Path(file).suffix,
        'size': stats.st_size,
        'doc': ''
    }

    _map: dict = client.update_record(voc.SCHEMAS, schema, map)
    
    client.tx_status('meta_builder', 'meta', _map[voc.ID], _map[voc.ITEM_PREFIX], voc.WAITING)

    return voc.OK

directory = "/home/alexmy/Downloads/Ontology/hackathon/demo"
for file in Path(directory).glob("**/*.csv"):
    ret = fileMeta(client, file, FILE)
    if ret != None:
        print('OK: {}'.format(file))
    else:
        print('Error updating: {}'.format(file))



