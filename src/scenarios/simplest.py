
from typing import Sequence
from base_classes.base_employee import BaseEmployee
from base_classes.base_employer import BaseEmployer
import random as rn

class SimplestEmployee(BaseEmployee):
    pass

class SimplestEmployer(BaseEmployer):

    def choose_hires(self, available_hires: Sequence[SimplestEmployee]) -> Sequence[SimplestEmployee]:
        return [rn.choice(available_hires)]
    
    def annual_gross_income(self) -> int:
        return sum([employee.productivity for employee in self.current_employees])

    def calculate_wage(self, employee: BaseEmployee):
        # Employees are paid exactly what they generate for the company - this is a very idealised scenario that does not represent the real world.
        # In real life, it's almost impossible to know exactly how much revenue employee generates for the company!
        return employee.productivity

    
    