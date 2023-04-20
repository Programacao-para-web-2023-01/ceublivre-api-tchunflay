from typing import Optional
from sqlmodel import Field, SQLModel, Session, create_engine, select

#create table model
class Products(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    category: str
    brand: str
    name: str
    description: str
    rate: Optional[float] = None
    price: float
    image: str

#create database based on above sqlmodel
engine = create_engine("sqlite:///database.db", echo=True)

def create_database():
    SQLModel.metadata.create_all(engine)

# insert into database with session
def insert_data():
    product1 = Products(category = "Videogame", brand = "Sony", name = "PS5", description = "Console mídia física + DUALSHOCK", rate = 4.7, price = 4599.99, image = "C:\program_web\database\5IjvCH5cYUSF8ePcjJm1KQ==.jpg")
    product2 = Products(category = "Videogame", brand = "Sony", name = "PS5", description = "Console mídia física + DUALSHOCK", rate = 4.3, price = 4999.99, image = "C:\program_web\database\5IjvCH5cYUSF8ePcjJm1KQ==.jpg")

    with Session(engine) as session:
        session.add(product1)
        session.add(product2)
        session.commit()

def main():
    create_database()
    insert_data()

def search():
    with Session(engine) as session:
        statement = select(Products)
        results = session.exec(statement)
        for product in results:
            return product

    