from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


class Product(Model):
    # converting this model into a table 
    __keyspace__="nh"
    asin=columns.Text(primary_key=True, required=True)
    title:str=columns.Text()
    price_str=columns.Text(default="-1")

class ProductScrapeEvent(Model):
    # converting this model into a table 
    __keyspace__="nh"
    uuid=columns.UUID(primary_key=True)
    asin=columns.Text(index=True)
    title:str=columns.Text()
    price_str=columns.Text(default="-100")

