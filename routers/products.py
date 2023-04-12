from tables.tb_products import *
from fastapi import FastAPI, HTTPException
from sqlmodel import Session, create_engine, select

app = FastAPI()

@app.get("/products/name")
async def get_products_by_name(name: str):
    with Session(engine) as session:
        statement = select(Products)
        results = session.exec(statement)
        for product in results:
            if len(product):
                return product

    raise HTTPException(status_code=404, detail="Product not found")
