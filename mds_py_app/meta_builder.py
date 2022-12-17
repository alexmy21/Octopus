from mds_py.mds_client import Client
from pathlib import Path

client = Client()
client.boot_strap()

print(client.boot)
print(client.schemas)
print(client.processors)

directory = "/home/alexmy/Downloads/Ontology/hackathon/demo"
for file in Path(directory).glob("**/*.csv"):
    print(file)