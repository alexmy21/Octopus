import redis

# from redis.commands.core import HyperlogCommands
from redis.commands.search.field import VectorField
from redis.commands.search.query import Query

from redis.commands.graph import Edge, Node, Path
from redis.commands.graph.execution_plan import Operation
from redis.commands.graph.query_result import QueryResult

r = redis.Redis(host='localhost', port=6379)

schema = (VectorField("v", "HNSW", {"TYPE": "FLOAT32", "DIM": 2, "DISTANCE_METRIC": "L2"}),)
r.ft().create_index(schema)

# value = ["a", "a", "a", "a", "a", "a",]
r.pfadd('vec1', 'a', 'a', 'a', 'a', 'a')
r.pfadd('vec2', 'a', 'a', 'a', 'a', 'a')
r.pfadd('vec3', 'a', 'a', 'c', 'a', 'b')

print(r.pfcount('vec'))

# print(r.dump('vec'))

# r.hset("a", "v", r.dump('vec1'))
# r.hset("b", "v", r.dump('vec2'))
# r.hset("c", "v", r.dump('vec3'))

r.hset("a", "v", "aaaaaaaa")
r.hset("b", "v", "aaaabaaa")
r.hset("c", "v", "aaaaabaa")


q = Query("*=>[KNN 3 @v $v]").return_field("__v_score").dialect(2)

print(r.ft().search(q, query_params={"vec": "aaaaaaaa"}))



