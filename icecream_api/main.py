from crud import write
from settings import MENU, QUANTITY

from typing import Dict
from datetime import datetime
from enum import Enum


class IceCream(Enum):
    VANILLA = 'vanilla'
    CHOCOLATE = 'chocolate'
    STRAWBERRY = 'strawberry'
    BANANA = 'banana'


def make_ice_cream(name: IceCream, money: int, user_name: str) -> Dict[str, str]:
    """готовит мороженное, сохраняет историю, забирает ресурсы"""
    if MENU.get(name) is None or MENU.get(name)['price'] > money:
        write('./history.txt', f"{datetime.now()}: {name} bought for {MENU[name]['price']} by {user_name} - Failed")
        return {"status": "no such ice cream or not enough money"}

    for ingredient in MENU[name]['recipe'].keys():
        if MENU[name]['recipe'][ingredient] > QUANTITY[ingredient]:
            write('./history.txt', f"{datetime.now()}: {name} bought for {MENU[name]['price']} by {user_name} - Failed")
            return {"status": "not enough resources"}

    for ingredient in MENU[name]['recipe'].keys():
        QUANTITY[ingredient] -= MENU[name]['recipe'][ingredient]

    money -= MENU[name]['price']
    write('./history.txt', f"{datetime.now()}: {name} bought for {MENU[name]['price']} by {user_name} - Done")

    return {"status": "done"}
