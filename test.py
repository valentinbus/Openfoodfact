import requests
import json
import pprint


pp = pprint.PrettyPrinter(indent=4)

with open('./local/categories.json', 'r') as file:
    data = file.read()
