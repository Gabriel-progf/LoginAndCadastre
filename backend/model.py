from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime

USER = "root"
PASSWORD = ""
HOST = "localhost"
PORT = "3306"
SCHEMA = "fastApidb"

CONN = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{SCHEMA}"


engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    password = Column(String(50))


class Token(Base):
    __tablename__ = "token"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    token = Column(String(50))
    date = Column(DateTime, default=datetime.utcnow())


Base.metadata.create_all(engine)
