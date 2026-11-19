import time
robot_state = {
    "status": "ожидание заказа",
    "temp": 22,
    "ingrend": {
    "тесто":5,
    "майонез":5,
    "сыр": 5,
    "пеперони": 5
},
    "current_pizza":[],
    "orders_completed": 0,
}

Avalable_toppings = ['сыр', 'Пеперони']

def get_status():
    return robot_state.copy()

def check_ingredients():
    inv = robot_state["ingrend"]
    return inv["тесто"] > 0 and inv['майонез'] > 0

def start_pizza():
    if not check_ingredients():
        return False, 'Недостаточно ингредиентов'
    robot_state['ingredients']['тесто']-=1
    robot_state['ingredients']['соус']-=1
    robot_state['current_pizza'] = ['основа из теста','соус']
    robot_state['status'] = 'Раскатываю тесто и нанесение соуса'
    return True, 'Основа для пиццы готова'

def add_topping(topping):
    if topping not in Avalable_toppings:
        return False, f'Ингредиент {topping} не поддерживается'
    if robot_state['ingredients'].get(topping, 0) <= 0:
        return False,f'Закончился ингридиент: {topping}'
    robot_state['ingredients'][topping] -= 1
    robot_state['current_pizza'].append(topping)
    robot_state['status'] = f'Добавление: {topping}'
    return True, f'Добавлено: {topping}'

def bake_pizza():
    if not robot_state['current_pizza']:
        return False, 'В печи пусто, сначала собери пиццу'
    robot_state['status'] = 'Начался разогрев печи...'
    robot_state['temp'] = 250
    time.sleep(2)
    finished_pizza = list(robot_state['current_pizza'])
    robot_state['current_pizza'] = []
    robot_state['temp'] = 22
    robot_state['status'] = 'Ожидает заказ...'
    robot_state['orders_completed'] += 1
    return True, finished_pizza

def restock_ingredients():
    for item in robot_state['ingredients']:
        robot_state['ingredients'][item] = 5
    robot_state['status'] = 'Запасы пополнены...'
    return 'Все  ингредиенты до 5 единиц'
