from fastavro import schemaless_writer
from fastavro.utils import generate_one

# schema = {
#     'doc': 'A weather reading.',
#     'name': 'Weather',
#     'namespace': 'test',
#     'type': 'record',
#     'fields': [
#         {'name': 'station', 'type': 'string'},
#         {'name': 'time', 'type': 'long'},
#         {'name': 'temp', 'type': 'int'},
#     ],
# }

schema = {
    "name": "MasterSchema",
    "namespace": "com.namespace.master",
    "type": "record",
    "fields": [{
        "name": "keys",
        "type": {
            "name": "Dependency",
            "namespace": "com.namespace.dependencies",
            "type": "record",
            "fields": [
                {"name": "sub_field_1", "type": "string"},
                {"name": "sub_field_2", "type": "string"},
                {"name": "sub_field_3", "type": "string"}
            ]
        }
    }, {
        "name": "params",
        "type": "com.namespace.dependencies.Dependency"
    }]
}

print(generate_one(schema))

# with open('weather.avro', 'wb') as out:
    
    # schemaless_writer(out, schema, generate_one(schema))

