import pytest

from app.controllers.report import ReportController
from app .controllers.beverage import BeverageController
from app.controllers.ingredient import IngredientController
from app.controllers.order import OrderController
from app.controllers.size import SizeController
from app.controllers.base import BaseController

from app.test.utils.functions import get_random_choice, shuffle_list


def __order(ingredients: list, beverages: list, size: dict, client_data: dict):
    ingredients = [ingredient.get('_id') for ingredient in ingredients]
    beverages = [beverage.get('_id') for beverage in beverages]
    size_id = size.get('_id')
    return {
        **client_data,
        'ingredients': ingredients,
        'size_id': size_id,
        'beverages': beverages
    }


def __create_items(items: list, controller: BaseController):
    created_items = []
    for ingredient in items:
        created_item, _ = controller.create(ingredient)
        created_items.append(created_item)
    return created_items


def __create_sizes_and_ingredients(ingredients: list, sizes: list, beverages: list):
    created_ingredients = __create_items(ingredients, IngredientController)
    created_sizes = __create_items(sizes, SizeController)
    created_beverages = __create_items(beverages, BeverageController)
    return created_sizes if len(created_sizes) > 1 else created_sizes.pop(), created_ingredients, created_beverages


def test_get_reports(client, report_uri, ingredients, sizes, client_data, beverages):
    created_sizes, created_ingredients, created_beverages = __create_sizes_and_ingredients(ingredients, sizes, beverages)
    created_orders = []
    for _ in range(5):
        order = __order(shuffle_list(created_ingredients)[:3], shuffle_list(created_beverages)[:3], get_random_choice(created_sizes), client_data)
        created_order, _ = OrderController.create(order)
        created_orders.append(created_order)

    response = client.get(report_uri)
    pytest.assume(response.status.startswith('200'))
    returned_report = response.json
    pytest.assume(returned_report['most_requested_ingredient'])
    pytest.assume(returned_report['top_3_customers'])
    pytest.assume(returned_report['month_with_more_revenue'])
