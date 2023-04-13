import tables.tb_products as DB
from fastapi import FastAPI, HTTPException
from sqlmodel import Session, create_engine, select

app = FastAPI()

@app.get("/products/name")
async def get_products_by_name(name: str):
    DB.main()
    res = DB.search()
    return res
    # raise HTTPException(status_code=404, detail="Product not found")
