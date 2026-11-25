import time
from main import *

def decorator(inputer):
    def outer(*args, **kwargs):
        print(28 * '*')
        inputer(*args, **kwargs)
        print(28 * '*')

    return outer


@decorator
def show_welcome():
    print('Робот пиццемейкер запускается...')


show_welcome()


def show_menu():
    print('Выберите действие: \n'
          '1. Сделать заказ \n'
          '2. Посмотреть статус и запасы робота\n'
          '3. Пополнить счет\n'
          '0. Выключить робота')


time.sleep(2)
print('Робот запущен!')
show_menu()

@decorator
def show_status(robot_state):
    print('Текущий статус робота\n'
          f'Состояние - {robot_state["status"]}\n'
          f'Температура печи - {robot_state["temp"]}°C\n'
          f'Выполнено заказов - {robot_state["orders_completed"]}\n'
          f'Остатки ингредиентов: \n')
    for item, count in robot_state['ingredients'].items():
        print(f' - {item.capitalize()}: {count} шт.')


def ask_menu_choice():
    return input('Ваш выбор: ').strip()

def ask_topping(Available_toppings):
    print(f'Доступные топпинги - {", ".join(Available_toppings)}\n'
          f'Введите нужные ингредиенты через запятую или нажмите Enter для пропуска')
    raw_input = input('> ').strip().lower()

    if not raw_input:
        return []
    return [item.strip() for item in raw_input.split(',') if item.strip()]


def show_message(message):
    print(f'[Информация]: {message}')


def show_error(error_message):
    print(f'[Ошибка]: {error_message}')


def show_finished_pizza(ingredients_list):
    print("Пицца готова !\n"
          f'Состав - {", ".join(ingredients_list)}\n'
          'Приятного аппетита!')
