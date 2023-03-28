from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import mysql.connector

cnx = mysql.connector.connect(user= 'root', password= "uniceub", host= 'localhost', database= 'product_list')

app = FastAPI()


class Product(BaseModel):
    id: Optional[int]
    name: str
    brand: str
    description: str
    rate: str
    category: str
    price: float


@app.get("/products/{name}")
async def get_products_by_name(name: str):
    cs = cnx.cursor(dictionary=True)
    query = f"SELECT * from `products` WHERE `product_name` = '{name}' ORDER BY `product_rate` DESC"

    cs.execute(query)
    l = cs.fetchall()
    if len(l) != 0:
        return l

    raise HTTPException(status_code=404, detail="product not found")

@app.get("/products/{brand}")
async def get_products_by_brand(brand:str):
    cs = cnx.cursor(dictionary=True)
    query = f"SELECT * from `products` WHERE `product_brand` = '{brand}' ORDER BY `product_rate` DESC"

    cs.execute(query)
    l = cs.fetchall()
    if len(l) != 0:
        return l

    raise HTTPException(status_code=404, detail="product not found")

#
# @app.get("/products")
# async def get_products_by_price(price:float):
#
#
# @app.get("/products")
# async def get_products_by_category(category:str):
#
#
# @app.get("/products")
# async def get_products_by_rate(rate:str):
