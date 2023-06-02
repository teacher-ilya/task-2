import json

from crud import read_file


MENU_PATH = './files/menu.json'
REGISTER_PATH  = './files/money.json'
QUANTITY_PATH = './files/quantity.json'

MENU = json.loads(read_file(MENU_PATH))
MONEY = json.loads(read_file(REGISTER_PATH))
QUANTITY = json.loads(read_file(QUANTITY_PATH))
