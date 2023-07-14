import os
import pathlib
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.cqlengine.connection import register_connection,set_default_connection

# from dotenv import load_dotenv
from app.db import config

settings=config.get_settings()


# load_dotenv()

client_id=settings.db_client_id
# client_secret=os.environ.get('clientSecret')
client_secret=settings.db_client_secret



BASE_DIR=pathlib.Path(__file__).parent.parent
CLUSTER_BUNDLE=str(BASE_DIR/"gitignore"/'connect.zip')


def get_cluster():
    cloud_config= {
    'secure_connect_bundle': CLUSTER_BUNDLE
    # '../gitignore/connect.zip'
    }
    auth_provider = PlainTextAuthProvider(client_id, client_secret)
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
   

    return cluster

def get_session():
    # gets session to connect with the database
    cluster=get_cluster()
    session = cluster.connect()
    register_connection(str(session),session=session)
    set_default_connection(str(session))
    
    return session

# session=get_session()
# row = session.execute("select release_version from system.local").one()
# if row:
#   print(row[0])
# else:
#   print("An error occurred.")
