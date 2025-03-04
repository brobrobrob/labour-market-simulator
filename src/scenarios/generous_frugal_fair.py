
from base_classes.base_employee import BaseEmployee
from scenarios.simplest import SimplestEmployer


class GenerousSimpleEmployer(SimplestEmployer):
    def calculate_wage(self, employee: BaseEmployee):
        return employee.productivity * 1.1
    
class FairSimpleEmployer(SimplestEmployer):
    def calculate_wage(self, employee: BaseEmployee):
        return employee.productivity * 0.9

class FrugalSimpleEmployer(SimplestEmployer):
    def calculate_wage(self, employee: BaseEmployee):
        return employee.productivity * 0.5