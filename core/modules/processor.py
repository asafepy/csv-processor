import argparse
import concurrent.futures
import json
import re
from multiprocessing import Process

from core.db.database import get_engine_db
from core.utils.file_util import cleanhtml


__author__ = 'asafe'


import os
import csv

class Processor(object):
	
	_file = None

	@classmethod
	def open_csv(self):
		
		with open(self._file, 'r') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
			for row in spamreader:
				print (', '.join(cleanhtml(row)))
	
	def get_article():
		pass

	def save_on_db():
		pass


if __name__ == "__main__":

	Processor._file = 'files/artigos.csv'
	results = Processor.open_csv()


# class Processor(object):
#     _test = False

#     @classmethod
#     def open_csv(self):
#         product_db = Product_db(get_engine_db(self._test))
#         products = product_db.get_products_for_status('WAIT')
#         return products

#     @classmethod
#     def parser_and_update(self, key, url):

#         content = Parser(url)
#         Product_db(get_engine_db(self._test)).update_product(
#             key, content.get_title(), content.get_name(), 'PROCESSED'
#         )

#     @classmethod
#     def run_processor(self):
        
#         processes = []
#         for product in self.get_urls():
#             if validate_url( product.url ):
#                 process = Process(target=self.parser_and_update, args=(product.id, product.url))
#                 processes.append(process)

#         for p in processes:
#             p.start()
        
#         for p in processes:
#             p.join()
    



# if __name__ == "__main__":


#     Processor.run_processor()

#     print('====== Processamento concluído ======')
    