import time

robot_state = {
    "status": "ожидание заказа",
    "temp": 22,
    "ingredients": {
        "тесто": 5,
        "соус": 5,
        "моцарелла": 5,
        "пармезан": 5,
        "чеддер": 5,
        "дорблю": 5,
        "фета": 5,
        "ветчина": 5,
        "бекон": 5,
        "курица": 5,
        "колбаски": 5,
        "креветки": 5,
        "томаты": 5,
        "перец": 5,
        "лук": 5,
        "руккола": 5,
        "базилик": 5,
        "шампиньоны": 5,
        "маслины": 5,
        "халапеньо": 5,
        "ананасы": 5,
        "огурцы": 5
    },

    "current_pizza": [],
    "orders_completed": 0,
}
Avalable_toppings = ['моцарелла', 'пармезан', 'чеддер', 'дорблю', 'фета', 'ветчина', 'бекон', 'курица', 'колбаски', 'креветки', 'томаты', 'перец', 'лук', 'руккола', 'базилик', 'шампиньоны', 'маслины', 'халапеньо', 'ананасы', 'огурцы']



def get_status():
    return robot_state.copy()


def check_ingredients():
    inv = robot_state["ingredients"]
    return inv["тесто"] > 0 and inv['соус'] > 0


def start_pizza():
    if not check_ingredients():
        return False, 'Недостаточно ингредиентов'
    robot_state['ingredients']['тесто'] -= 1
    robot_state['ingredients']['соус'] -= 1

    robot_state['current_pizza'] = ['основа из теста', 'соус']
    robot_state['status'] = 'Раскатываю Comic-тесто и нанесение соуса'
    return True, 'Основа для пиццы готова'


def add_topping(topping):
    topping_lower = topping.lower()
    if topping_lower not in Avalable_toppings:
        return False, f'Ингредиент {topping} не поддерживается'
    if robot_state['ingredients'].get(topping_lower, 0) <= 0:
        return False, f'Закончился ингредиент: {topping}'
    robot_state['ingredients'][topping_lower] -= 1
    robot_state['current_pizza'].append(topping_lower)
    robot_state['status'] = f'Добавление: {topping_lower}'
    return True, f'Добавлено: {topping_lower}'


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
    return 'Все ингредиенты до 5 единиц'
