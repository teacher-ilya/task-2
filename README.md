[![flake8](https://github.com/Private-Python-Class/task-2-icecream/actions/workflows/lint-test.yml/badge.svg)](https://github.com/Private-Python-Class/task-2-icecream/actions/workflows/lint-test.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/c44186e21b0461afb6f2/maintainability)](https://codeclimate.com/github/Private-Python-Class/task-2-icecream/maintainability)

# Аппарат для изготовления мороженного

## Предыстория
В 2028 году Макдональдс начал выпускать аппараты для изготовления мороженного и вашей команде поручили написать код для работы этого аппарата.

## Функционал

Программа должна уметь:
* предлагать пользователю выбор мороженного из меню
* проверять количество ингредиентов и посылать команду на изготовление мороженного
* принимать оплату наличными и по карте
* история покупок сохраняется в ```history.txt```
* количество купюр и монет сохраняется в ```money.json```
* ингридиенты и их количество храниться в ```quantity.json```


## Условия

* Вывод сообщений производится с помощью функции ```send_message()```, в коде не используется ```print```
* Ввод производиться с помощью функции ```get_input```
* Тесты должны работать
* Запуск программы производится через ```main.py```
* Не должно быть ошибок линтера
* Качество кода должно быть выше, чем оценка D
