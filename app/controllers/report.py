from sqlalchemy.exc import SQLAlchemyError
from app.controllers.base import BaseController
from app.repositories.managers import ReportCreator, MostRequestedIngredient, Top3Customers, MonthWithMoreRevenue


class ReportController(BaseController):
    
    @classmethod
    def get_report_data(report_creator):
        try:
            most_requested_ingredient = MostRequestedIngredient.return_report()
            top_3_customers = Top3Customers.return_report()
            month_with_more_revenue = MonthWithMoreRevenue.return_report()

            return {
                'most_requested_ingredient': most_requested_ingredient, 
                'top_3_customers': top_3_customers,
                'month_with_more_revenue': month_with_more_revenue
            }, None
                
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)