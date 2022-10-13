from app.common.http_methods import GET
from flask import Blueprint, jsonify

from app.controllers.report import ReportController
from .base_service import base_service


report = Blueprint('report', __name__)


@report.route('/', methods=GET)
def get_report():
    data, error = ReportController.get_report_data()
    response = data if not error else {'error': error}
    status_code = 200 if data else 404 if not error else 400
    return jsonify(tuple(response)), status_code