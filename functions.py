from menu import menu
from money import money
from quantity import quantity

########### finished ###########
def send_message(text: str) -> None:
	"""Аппарат отправляет сообщеине пользователю"""
	print(text)

def get_input(message: str) -> str:
	"""Функция принимает ответ от пользователя"""
	return input(message), input('Наличными или по карте')

def send_report() -> None:
	"""Отправляет емайл администратору, что нет ингредиентов"""
	pass

def is_made_ice_cream() -> bool:
  	"""Возвращает True если мороженное было изготовлено"""
  	return True
########### finished ###########

def make_icecream(cost, recipe):
    for i in recipe.keys():
        if quantity[i] - recipe[i] < 0:
            send_report()
            return False
    # we have materials
    return True


def money(cost: int):
    """Делает работу с деньгами"""
    pass

def history(time, name, cost, is_done): 
    """Записывает в историю действия"""
    file = open('history.txt', 'a')
    file.write(f"{time}: {name} bought for {cost} - {is_done}")
    file.close()


# TODO: make a main function
# def main(menu):
#     """Делает мороженые и основную работу"""
#     for i in menu:
#         is_done = make_icecream(i["name"], i["cost"], i['recipe']) 
#         if is_done == True:
#             history(menu.index(i), i["name"], i['cost'], 'Nice')
#         else:
#             history(menu.index(i), i["name"], i['cost'], 'Error')
        

buyers_message = get_input("Выберите номер того что вы хотите купить из меню")
