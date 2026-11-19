import time


def decorator(inputer):
    def outer():
        print(28*'*')
        inputer()
        print(28*'*')
    return outer

@decorator
def show_welcome():
    print('Робот пиццемейкер запускается...')
show_welcome()

def show_menu():
    print('Выберите действие: \n',
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
          f'Температура печи {state["temp"]}\n'
          f'Выполнено заказов {state["orders_completed"]}\n'
          f'Остатки ингредиентов: \n')
    for  item, count in robot_state['ingredients'].items():
        print(f' - {item.capitalize()}:{count} шт.')

def ask_menu_choice():
    return input('Ваш выбор: ').strip()

def ask_topping(available_toppings):
    print(f'Доступные топпинги - {", ".join(available_toppings)}\n'
          f'Введите нужные ингредиенты через запятую или нажмите Entre для пропуска')
    raw_input = input('> ').sprit().lower()

    if not raw_input:
        return []
    return [item.strip()]

def show_message(message):
    print(f'[Информация]: {message}')

def show_error(error_message):
    print(f'[Ошибка]: {error_message}')

def show_finished_pizza(ingredients_list):
    print("Пицца готова !\n"
          f'Состав - {", ".join(ingredients_list)}'
          'Приятного аппетита!')



