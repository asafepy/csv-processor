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
from core.db.model import Article

__author__ = 'asafe'

csv.field_size_limit(sys.maxsize)

class Processor(object):
	
	_file = None
	_db = None

	@staticmethod
	def save_on_db(row_csv, db):
	
		article = Article(title = row_csv['title'], descricao = row_csv['descricao'], dtPublicacao = row_csv['dtPublicacao'], idIdioma = row_csv['idIdioma'], idArtigoPai = row_csv['idArtigoPai'])

		db.add(article)
		db.commit()
		
	@classmethod
	def open_csv(self):
		columns = defaultdict(list)
		with open(self._file, 'r') as csvfile:
			spamreader = csv.DictReader(csvfile)
			for row in spamreader:
				for (k,v) in row.items():
					columns[k].append(cleanhtml(v))	
		return columns
	
	@classmethod
	def run_processor(self):
		
		if( self._db is not None ):
			for article in self.open_csv():
				self.save_on_db(article, self._db)
				print('success')


if __name__ == "__main__":

	Processor._file = 'files/artigos.csv'
	Processor._db = Session(bind=get_engine_db())
	Processor.run_processor()
