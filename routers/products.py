import tables.tb_products as DB
from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select

app = FastAPI()
DB.main()

@app.get("/products")
async def get_products():
   res = DB.search_products()
   if DB.search_products() == None:
      raise HTTPException(status_code=404, detail="Product not found")
   
   return res

@app.get("/products")
async def get_products_by_name(name: str = '', category: str = '', brand: str = '', description = '', rate = ''):
   with Session(DB.engine) as session:
      statement = select(DB.Products).where(DB.Products.name == name or DB.Products.category == category or DB.Products.brand == brand or DB.Products.descript == description or DB.Products.rate == rate)
      results = session.exec(statement).all()
      if results == None:
         raise HTTPException(status_code=404, detail="Product not found")
    
      return results
   

@app.get("/categories")
async def get_categories():
   res = DB.search_categories()
   if DB.search_categories() == None:
      raise HTTPException(status_code=404, detail="Product not found")
    
   return res
