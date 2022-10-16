

import pytest
from flask.cli import FlaskGroup
from flask_migrate import Migrate

from app import flask_app
from app.plugins import db
# flake8: noqa
from app.repositories.models import Ingredient, Order, OrderDetail, Size, Beverage
from app.dummy_data import dummy_data_creator


manager = FlaskGroup(flask_app)


migrate = Migrate()
migrate.init_app(flask_app, db)


@manager.command('orders', with_appcontext=True)
def dummy_orders():
    '''
    Populates the database with dummy orders.
    See dummy_data_creator for implemention details.
    '''
    return  dummy_data_creator.main()


@manager.command('test', with_appcontext=False)
def test():
    return pytest.main(['-v', '--cov=app/', './app/test'])


if __name__ == '__main__':
    manager()
