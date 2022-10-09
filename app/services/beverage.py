from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from app.controllers.beverage import BeverageController
from .base_service import base_service

beverage = Blueprint('beverage', __name__)


@beverage.route('/', methods=POST)
def create_beverage():
    return base_service(BeverageController.create(request.json))


@beverage.route('/', methods=PUT)
def update_beverage():
    return base_service(BeverageController.update(request.json))


@beverage.route('/id/<_id>', methods=GET)
def get_beverage_by_id(_id: int):
    return base_service(BeverageController.get_by_id(_id))


@beverage.route('/', methods=GET)
def get_beverages():
    return base_service(BeverageController.get_all())
