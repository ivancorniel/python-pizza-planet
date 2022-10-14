from app.common.http_methods import GET
from flask import Blueprint
from .base_service import base_service

from app.controllers.report import ReportController


report = Blueprint('report', __name__)


@report.route('/', methods=GET)
def get_report():
    return(base_service(ReportController.get_report_data()))

    