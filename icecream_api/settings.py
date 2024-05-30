import json
from crud import read


MENU = dict(json.loads(read('./data/menu.json')))
QUANTITY = dict(json.loads(read('./data/quantity.json')))
