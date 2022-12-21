import os
import pathlib
import mds_py.mds_utils as utl
from mds_py.mds_client import Client
from mds_py.mds_vocabulary import Vocabulary as voc
from pathlib import Path

directory = "/home/alexmy/Downloads/Ontology/hackathon/demo"

client = Client()
client.bootstrap()

schema = client.schema_file_name(voc.SCHEMAS, voc.FILE)
client.create_index(voc.SCHEMAS, voc.FILE)

if __name__ == "__main__":
    for file in Path(directory).glob("**/*.csv"):
        print('HEADER: {}'.format(utl.csvHeader(file)))
        ret = client.file_meta('file_meta', 'meta', file)
        if ret == None:
            print('Error updating: {}'.format(file))
