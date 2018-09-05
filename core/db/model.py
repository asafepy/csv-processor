from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import ChoiceType

__author__ = 'asafe'

Base = declarative_base()

class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True)
    titulo = Column(String,  nullable=True)
    descricao = Column(String,  nullable=True)
    dt_publicacao = Column(String,  nullable=True)
    id_idioma = Column(Integer,  nullable=True)
    id_artigoPai = Column(Integer,  nullable=True)


class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    id_idioma = Column(Integer,  nullable=True)
    id_usuario = Column(Integer,  nullable=True)
    id_usuario_modificacao = Column(Integer,  nullable=True)
    titulo = Column(String,  nullable=True)
    chamada = Column(String,  nullable=True)
    conteudo = Column(String,  nullable=True)
    imagem = Column(String,  nullable=True)
    legenda = Column(String,  nullable=True)
    link = Column(String,  nullable=True)
    data = Column(String,  nullable=True)
    data_modificacao = Column(String,  nullable=True)
    exibir = Column(String,  nullable=True)
    miniatura = Column(String,  nullable=True)
    imagem_chamada = Column(String,  nullable=True)
    novidade = Column(String,  nullable=True)