import os
import time
import argparse

# for key in os.environ.keys():
#    print ( "key->{}< value->{}<".format( key , os.environ[ key ] ) )

parser = argparse.ArgumentParser()
parser.add_argument("--redis_password", default="password", type=str)
args = parser.parse_args()

if os.environ[ "AZ_BATCH_IS_CURRENT_NODE_MASTER" ] == "true":
    print( "master node" )
    os.system( "ray start --head --redis-port=6000 --redis-password='password'" )
    print ( "sleeping" )
    time.sleep ( 60 )
    print ( "waking up and running script" )
    os.system( "python ray_cluster_addrs.py --redis_address {} --redis_password='password'".format( os.environ[ "AZ_BATCH_MASTER_NODE" ] ,
                                                                                                        args.redis_password ) )
else:
    print( "worker node" )
    os.system( "ray start --redis-address={} --redis-password='password'".format( os.environ[ "AZ_BATCH_MASTER_NODE" ] ,
                                                                                                        args.redis_password ) )