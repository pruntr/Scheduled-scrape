from fastapi import FastAPI
from typing import List

from cassandra.cqlengine.management import sync_table


from . import (
    config,db,models,schema,crud
)

settings=config.get_settings()
Product = models.Product
ProductScrapeEvent = models.ProductScrapeEvent

app=FastAPI()

session=None

@app.on_event("startup")
def on_startup():
    global session
    session=db.get_session()
    sync_table(models.Product)
    sync_table(models.ProductScrapeEvent)

@app.get("/")
def read_index():
    return {"hello":"world"}

@app.get("/products",response_model=List[schema.ProductListSchema])
def product_list_view():
    return list(models.Product.objects.all())

@app.get("/products/{asin}")
def product_list_view(asin):
    data= dict(models.Product.get(asin=asin))
    events=list(ProductScrapeEvent.objects().filter(asin=asin))
    events=[schema.ProductScrapeEventDetailSchema(**x) for x in events]
    data['events']=events
    return data


# @app.get("/")
# def read_index():
#     return {"hello":"world"}