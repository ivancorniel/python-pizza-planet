from app.common.http_methods import GET, POST
from flask import Blueprint, request

from ..controllers import OrderController
from .base_service import base_service

order = Blueprint('order', __name__)


@order.route('/', methods=POST)
def create_order():
    return base_service(OrderController.create(request.json))


@order.route('/id/<_id>', methods=GET)
def get_order_by_id(_id: int):
    return base_service(OrderController.get_by_id(_id))


@order.route('/', methods=GET)
def get_orders():
    return base_service(OrderController.get_all())
