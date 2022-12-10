# print_json.py

# import datetime
# import json

# person = {
#     "firstName": "John",
#     "dateOfBirth": datetime.date(1969, 12, 31),
#     "married": False,
#     "spouse": None,
#     "children": ["Bobby", "Molly"],
# }

# print(json.dumps(person, indent=4, default=str))

from ensure import Ensure
from strictyaml import as_document
from collections import OrderedDict

# Can also use regular dict if an arbitrary ordering is ok
yaml = as_document(OrderedDict(
    [(u"â", 'yes'), ("b", "hâllo"), ("c", ["1", "2", "3"])]
))

print(yaml.as_yaml())