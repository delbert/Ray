import os
import time
import argparse

import ray

parser = argparse.ArgumentParser()
parser.add_argument("--redis_address", default="localhost", type=str)
parser.add_argument("--redis_password", default="password", type=str)
args = parser.parse_args()

ray.init( redis_address = args.redis_address , redis_password = args.redis_password ) 

@ray.remote
def f():
    time.sleep(0.01)
    return ray.services.get_node_ip_address()

# Get a list of the IP addresses of the nodes that have joined the cluster.
print( "addresses in cluster->{}<".format( set( ray.get( [f.remote() for _ in range( 1000 ) ] ) ) ) )