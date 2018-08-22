from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import ChoiceType

__author__ = 'asafe'

Base = declarative_base()

class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True)
    title = Column(String,  nullable=True)
    descricao = Column(String,  nullable=True)
    dtPublicacao = Column(String,  nullable=True)
    dtPublicacao = Column(String,  nullable=True)
    idIdioma = Column(String,  nullable=True)
    idArtigoPai = Column(String,  nullable=True)
    name = Column(String,  nullable=True)