#!/usr/bin/env python

import os
import csv
from jinja2 import Template, FileSystemLoader, Environment

env = Environment(loader = FileSystemLoader('templates'))

input_file = 'values.csv'
output_dir = 'output'

cfg_template = env.get_template('config.tmpl')

with open(input_file) as cv:
	reader = csv.DictReader(cv)
	for row in reader:
		output_file = os.path.join(output_dir, row['HOSTNAME'] + '.cfg')
		with open(output_file, 'w') as of:
			of.write(cfg_template.render(**row))


