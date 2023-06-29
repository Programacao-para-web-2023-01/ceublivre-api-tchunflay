import tables.tb_products as DB
from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select
from sqlalchemy import or_, desc

app = FastAPI()
DB.main()

@app.get("/products/all")
async def get_products():
   res = DB.search_products()
   if DB.search_products() == None:
      raise HTTPException(status_code=404, detail="Product not found")
   
   return res

@app.get("/products")
async def get_products_by_name(name: str = '', category: str = '', brand: str = '', description = ''):
   with Session(DB.engine) as session:
      statement = select(DB.Products).where(or_(DB.Products.p_name == name, DB.Products.category == category, DB.Products.brand == brand, DB.Products.descript.like == description)).order_by(desc(DB.Products.rate))
      results = session.exec(statement).all()
      if not results:
         raise HTTPException(status_code=404, detail="Product not found")
    
      return results
   

@app.get("/categories")
async def get_categories():
   res = DB.search_categories()
   if DB.search_categories() == None:
      raise HTTPException(status_code=404, detail="Product not found")
    
   return res
