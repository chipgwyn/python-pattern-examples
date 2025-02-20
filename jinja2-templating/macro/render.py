#!/usr/bin/env python3

import yaml
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader

env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape()
)

with open('data.yml') as YML:
    data = yaml.safe_load(YML)

print(data)

template = env.get_template('config.j2')
output = template.render(data=data)
print(output)

