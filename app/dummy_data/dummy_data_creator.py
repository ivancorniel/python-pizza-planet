from random import randint

from app.test.utils.functions import *

from app.controllers.size import SizeController
from app.controllers.ingredient import IngredientController
from app.controllers.order import OrderController


def main():

    client_names = ['Ivan', 'Marco', 'Ricardo', 'Dylan', 'David', 'Wladimyr','Fausto', 'Gustavo', 'Astrid', 'Marievelyn', 'Mary', 'Brandy', 'Lucas', 'Roland', 'Israel']

    def client_dummy_data() -> dict:
        return {
            'client_address': get_random_string(),
            'client_dni': get_random_sequence(),
            'client_name': client_names[randint(0, len(client_names) - 1)],
            'client_phone': get_random_sequence()
        }
    
    def get_sizes():
        sizes, error = SizeController.get_all()
        return sizes

    def get_ingredients():
        ingredients, error = IngredientController.get_all()
        return ingredients

    def create_orders() -> list:
        ingredients = [ingredient.get('_id') for ingredient in get_ingredients()]
        sizes = [size.get('_id') for size in get_sizes()]
        orders = []
        for _ in range(1):
            new_order = {
                **client_dummy_data(),
                'ingredients': shuffle_list(ingredients)[:5],
                'size_id': shuffle_list(sizes)[0]
            }
            orders.append(new_order)
        
        [OrderController.create(order) for order in orders]

    return create_orders()
