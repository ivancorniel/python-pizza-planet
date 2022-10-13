from sqlalchemy.exc import SQLAlchemyError
from app.controllers.base import BaseController
from app.repositories.managers import ReportManager


class ReportController(BaseController):
    
    @classmethod
    def get_report_data(cls):
        try:
            most_requested_ingredient = ReportManager.get_most_requested_ingredient()
            top_3_customers = ReportManager.get_top_3_customers()
            month_with_more_revenue = ReportManager.get_month_with_more_revenue()

            return {
                'most_requested_ingredient': most_requested_ingredient, 
                'top_3_customers': top_3_customers,
                'month_with_more_revenue': month_with_more_revenue
            }, None
                
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)