import concurrent.futures
import argparse
import json
import re
import os
import csv
import sys

from sqlalchemy.orm import Session
from multiprocessing import Process
from core.db.database import get_engine_db
from core.utils.file_util import cleanhtml
from collections import defaultdict
from core.db.model import Article, News
from glob import glob


__author__ = 'asafe'
path = 'files/'
csv.field_size_limit(sys.maxsize)

class Processor(object):
	
	_file = None
	_db = None

	@staticmethod
	def save_on_db(row_csv, ind, db):
		# data = News(id_idioma = row_csv['id_idioma'][ind], titulo = row_csv['titulo'][ind], chamada = row_csv['chamada'][ind], conteudo = row_csv['conteudo'][ind], imagem = row_csv['imagem'][ind], legenda = row_csv['legenda'][ind], link = row_csv['link'][ind], data = row_csv['data'][ind], data_modificacao = row_csv['data_modificacao'][ind], exibir = row_csv['exibir'][ind], miniatura = row_csv['miniatura'][ind], imagem_chamada = row_csv['imagem_chamada'][ind], novidade = row_csv['novidade'][ind])
		data = Article(titulo = row_csv['titulo'][ind], descricao = row_csv['descricao'][ind], dt_publicacao = row_csv['dtPublicacao'][ind], id_idioma = row_csv['idIdioma'][ind])
		db.add(data)
		db.commit()
		
	@classmethod
	def open_csv(self):
		columns = defaultdict(list)
		count = 0
		with open(self._file, 'r') as csvfile:
			spamreader = csv.DictReader(csvfile)
			for row in spamreader:
				for (k,v) in row.items():
					columns[k].append(cleanhtml(v))	
				count += 1
		
		return (columns, int(count))
	
	@classmethod
	def run_processor(self):
		
		if( self._db is not None ):
			articles, count = self.open_csv()

			for ind in range(0, count):
				# print(len(articles['titulo']))
				self.save_on_db(articles, ind, self._db)
			print('success')


if __name__ == "__main__":
	
	# for file in glob(path+"*.csv"):

	Processor._file = 'files/article.csv'
	Processor._db = Session(bind=get_engine_db())
	Processor.run_processor()
