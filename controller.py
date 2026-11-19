import main
import views

def handle_make_pizza():
    succes, msg = main.start_pizza
    if not succes:
        views.show_error(msg)
        return
    views.show_message(msg)
    chosen_toppings = views.ask_topping(main.Avalable_toppings)
    for topping in chosen_toppings:
        if topping:
            ok, top_msg = main.add_topping(topping)
            if ok:
                views.show_message(top_msg)
            else:
                views.show_message(top_msg)

    views.show_message('Отправляем пиццу в печь...')
    baked, res = main.bake_pizza()
    if baked:
        views.show_finished_pizza(res)
    else:
        views.show_error(res)

def handle_show_status():
    current_state = main.get_status()
    views.show_status(current_state)

def handle_restock():
    mgs = main.restock_ingredients()
    views.show_message(mgs)

def run_robot():
    views.show_welcome()
    choice = views.ask_menu_choice()
    while True:
        if choice == '1':
            handle_make_pizza()
        elif choice == '2':
            handle_show_status()
        elif choice == '3':
            handle_restock()
        elif choice == '0':
            views.show_message('Выключение системы...')
            break
        else:
            views.show_error('Неизвестная команда')

