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
            session.add(Category(C_name=category))
            session.commit()


    products = [("Gaming", "Sony", "PS5", "Console mídia física + DualSense", 4.7, 4599.99, "https://tfcvih.vtexassets.com/arquivos/ids/159380-264-264?v=638212412666970000&width=264&height=264&aspect=true"),
    ("Gaming", "Sony", "PS5", "Console mídia física + DualSense", 4.3, 4999.99, "https://tfcvih.vtexassets.com/arquivos/ids/159380-264-264?v=638212412666970000&width=264&height=264&aspect=true"),
    ("Gaming", "Microsoft", "Xbox Series S", "Console Xbox Series S 512GB", 4.5, 3699.99, "https://www.kabum.com.br/conteudo/descricao/128561/img/Console_Xbox_One_S_1.png"),
    ("Livros", "Rocco", "Jogos Vorazes", "Livro Juvenil Fantasia", 4.4, 42.99, "https://leitura.com.br/image/cache/products/9788579800245-500x500.jpg"),
    ("Livros", "Intrinseca", "Percy Jackson e os Olimpianos BUNDLE", "Série de Livros Percy Jackson e os Olimpianos, Juvenil Mitologia", 4.8, 412.63, "https://papelarianobel.com.br/wp-content/uploads/2021/08/Percy-1.jpg"),
    ("Papelaria", "Faber Castell", "Caixa de Lápis de Cor Pequena", "Lápis de Cor Faber Castell 12 Cores + 6 Cores Neon", 4.2, 23.54, "https://m.media-amazon.com/images/I/61RnETDeHNL._AC_UF894,1000_QL80_.jpg"),
    ("Papelaria", "Tilibra", "Caderno Tilibra Universe", "Caderno Tilibra 96 páginas, folha branca", 3.8, 17.90, "https://images.tcdn.com.br/img/img_prod/1106500/caderno_tilibra_universitario_magic_16_materias_15723_1_e3698c5c6a66256c902e06957d93eecb.jpg"),
    ("Acessórios", "Doxa", "Relógio Doxa Aquamarine", "Relógio Doxa Aquamarine Diver Masculino, tamanho ajustável prata", 3.6, 245.50, "https://www.thauro.com.br/media/catalog/product/cache/1/image/a4811146157e663113d10d64ad7ef273/r/e/relo_gio_doxa_sub200_aquamarine_diver_200m_799.10.241.10_caixa_42mm_capa_thauro_relogios.jpeg"),
    ("Acessórios", "Bontrager", "Luvas Bontrager Velocis", "Luvas Pretas Ciclismo Masculina Dedo Longo", 4.0, 290.00, "https://www.tuttobike.com.br/media/catalog/product/cache/1/image/980x/9df78eab33525d08d6e5fb8d27136e95/l/u/luva-bontrager-velocis-gel-ciclismo-masculina-dedo-longo-preto-bontrager.jpg"),
    ("Acessórios","-", "Anel de Cruz","Anel Prata de Cruz Retrô Tamanho Ajustável" ,2.3 ,173.70 ,"https://m.media-amazon.com/images/I/41DkU9mHHbS._AC_UF894,1000_QL80_.jpg"),
    ("Roupa Masculina","Levis","Bermuda Jeans Levis","Bermuda Masculina Jeans Levis Tamanho M" ,3.4 ,179.90 ,"https://static.dafiti.com.br/p/Levis-Bermuda-Jeans-Levis-Destroyed-Azul-5070-0104811-3-zoom.jpg"),
    ("Roupa Feminina","Western","Bota Feminina Western Preto","Bota Feminina Cano Alto Preta Western 37" ,3.7 ,329.90 ,"https://cdn.shoppub.io/cdn-cgi/image/w=1000,h=1000,q=80,f=auto/vicerinne/media/uploads/produtos/foto/gvlygsuk/vicerinne-23-02-23-13-a.jpg"),
    ("Roupa Feminina","Carlos Miele","Vestido Longo Goiaba","Vestido Curto Carlos Miele Goiaba M" ,3.9 ,420.99 ,"https://cdnimg.etiquetaunica.com.br/products/vestido-de-festa-carlos-miele-plissado-seda-goiaba-fhm20_159508.jpg")
    ]

    with Session(engine) as session:
        for product in products:
            session.add(Products(category=product[0], brand=product[1], p_name=product[2], descript=product[3], rate=product[4], price=product[5], image=product[6]))
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

