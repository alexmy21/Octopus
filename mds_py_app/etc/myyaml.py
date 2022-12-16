# from schema import Schema, SchemaError
# import yaml
# config_schema = Schema({
#     "api": {
#         "token": str
#     }
# })
# conf_yaml = """
# api:
#     token: 625c2043c132485b
# """
# configuration = yaml.safe_load(conf_yaml)
# try:
#     config_schema.validate(configuration)
#     print("Configuration is valid.")
# except SchemaError as se:
#     raise se

# import yaml
# import json

# with open('config.yml', 'r') as file:
#     configuration = yaml.safe_load(file)

# with open('config.json', 'w') as json_file:
#     json.dump(configuration, json_file)
    
# output = json.dumps(json.load(open('config.json')), indent=2)
# print(output)

import yaml
import json

with open('config.json', 'r') as file:
    configuration = json.load(file)

with open('config.yaml', 'w') as yaml_file:
    yaml.dump(configuration, yaml_file)

with open('config.yaml', 'r') as yaml_file:
    print(yaml_file.read())