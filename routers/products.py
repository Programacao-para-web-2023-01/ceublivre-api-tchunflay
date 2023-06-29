import tables.tb_products as DB
from fastapi import FastAPI, HTTPException
from sqlmodel import Session, create_engine, select

app = FastAPI()

@app.get("/products")
async def get_products_by_name(name: str = '', category: str = '', brand: str = '', description = '', rate = ''):
    res = DB.search_products()
    if DB.search_products() == None:
       raise HTTPException(status_code=404, detail="Product not found")
    
    return res

@app.get("/categories")
async def get_categories():
    res = DB.search_categories()
    if DB.search_categories() == None:
       raise HTTPException(status_code=404, detail="Product not found")
    
    return res
