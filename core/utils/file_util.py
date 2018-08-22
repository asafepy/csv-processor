import csv
import os
import re

__author__ = 'asafe'


def has_header(file, header):
    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if list(row) != header:
                raise ValueError('invalid header')

            return True


def add_header(file, header):
    with open(file, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(header)

def open_csv(file):
    with open(file, 'r') as csvfile:
        read = csv.read(csvfile, delimiter=',')


def create_file(file, header):
    if not os.path.exists(file):
        add_header(file, header)
    else:
        if not has_header(file, header):
            add_header(file, header)


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', self.raw_html)
    return cleantext