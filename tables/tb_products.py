from typing import Optional
from sqlmodel import Field, SQLModel, Session, create_engine, select
from dotenv import load_dotenv
import os

load_dotenv()
connection_string = f'mysql+mysqlconnector://{os.environ.get("USER")}:{os.environ.get("PASSWORD")}@{os.environ.get("HOSTNAME")}:3306/{os.environ.get("DATABASE")}'

#create table model
class Products(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    category: str
    brand: str
    p_name: str
    descript: str
    rate: Optional[float] = None
    price: float
    image: str

class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    C_name: str

#create database based on above sqlmodel
engine = create_engine(connection_string, echo=True)

def create_database():
    SQLModel.metadata.create_all(engine)

# insert data with session
def insert_data():
    categories = ["Gaming", "Livros", "Papelaria", "Acessórios", "Roupa Masculina", "Roupa Feminina", "PetShop", "Eletrônicos", "Esportes"]
    
    with Session(engine) as session:
        for category in categories:
            session.add(Category(name=category))
            session.commit()


    products = [("Gaming", "Sony", "PS5", "Console mídia física + DualSense", 4.7, 4599.99, "C:\program_web\database/5IjvCH5cYUSF8ePcjJm1KQ==.jpg"),
    ("Gaming", "Sony", "PS5", "Console mídia física + DualSense", 4.3, 4999.99, "C:\program_web\database\/5IjvCH5cYUSF8ePcjJm1KQ==.jpg"),
    ("Gaming", "Microsoft", "Xbox Series S", "Console Xbox Series S 512GB", 4.5, 3699.99, "C:\program_web\database\Xbox.jpg"),
    ("Livros", "Rocco", "Jogos Vorazes", "Livro Juvenil Fantasia", 4.4, 42.99, "C:\program_web\database\jogos-vorazes.jpg"),
    ("Livros", "Intrinseca", "Percy Jackson e os Olimpianos BUNDLE", "Série de Livros Percy Jackson e os Olimpianos, Juvenil Mitologia", 4.8, 412.63, "C:\program_web\database\percyjackson.jpg"),
    ("Papelaria", "Faber Castell", "Caixa de Lápis de Cor Pequena", "Lápis de Cor Faber Castell 12 Cores + 6 Cores Neon", 4.2, 23.54, "C:\program_web\database\lapis.jpg"),
    ("Papelaria", "Tilibra", "Caderno Tilibra Universe", "Caderno Tilibra 96 páginas, folha branca", 3.8, 17.90, "C:\program_web\database\caderno.jpg"),
    ("Acessórios", "Doxa", "Relógio Doxa Aquamarine", "Relógio Doxa Aquamarine Diver Masculino, tamanho ajustável prata", 3.6, 245.50, "C:\program_web\database\doxa.jpg"),
    ("Acessórios", "Bontrager", "Luvas Bontrager Velocis", "Luvas Pretas Ciclismo Masculina Dedo Longo", 4.0, 290.00, "C:\program_web\database\luvas.jpg"),
    ("Acessórios","-", "Anel de Cruz","Anel Prata de Cruz Retrô Tamanho Ajustável" ,2.3 ,173.70 ,"C:\program_web\database/anel.jpg"),
    ("Roupa Masculina","Levis","Bermuda Jeans Levis","Bermuda Masculina Jeans Levis Tamanho M" ,3.4 ,179.90 ,"C:\program_web\database/berm.jpg"),
    ("Roupa Feminina","Western","Bota Feminina Western Preto","Bota Feminina Cano Alto Preta Western 37" ,3.7 ,329.90 ,"C:\program_web\database/botaf.jpg"),
    ("Roupa Feminina","Carlos Miele","Vestido Longo Goiaba","Vestido Curto Carlos Miele Goiaba M" ,3.9 ,420.99 ,"C:\program_web\database/vest.jpg")
    ]

    with Session(engine) as session:
        for product in products:
            session.add(Products(category=product[0], brand=product[1], name=product[2], description=product[3], rate=product[4], price=product[5], image=product[6]))
            session.commit()


def main():
    create_database()
    insert_data()

def search_products():
    with Session(engine) as session:
        statement = select(Products)
        results = session.exec(statement).all()
        return results

def search_categories():
    with Session(engine) as session:
        statement = select(Category)
        results = session.exec(statement).all()
        return results

