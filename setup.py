__author__ = 'asafe'
import pytest

from distutils.core import setup

setup(
    name='csv-processor',
    version='1.0',
    description='CSV Processor',
    author='asafe',
    author_email='asafeao@if.uff.br',
    url='https://github.com/asafepy/csv-processor.git',
    packages=[
      'core',
      'core.db',
      'core.modules',
      'core.utils',
      'config',
    ],
)