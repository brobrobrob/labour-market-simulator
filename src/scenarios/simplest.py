
from typing import List
from base_classes.base_employee import BaseEmployee
from base_classes.base_employer import BaseEmployer
import random as rn

class SimplestEmployee(BaseEmployee):
    pass

class SimplestEmployer(BaseEmployer):
    
    def annual_gross_income(self):
        return sum([employee.productivity for employee in self.current_employees])
    
    def choose_hires(self, available_hires: List[SimplestEmployee]) -> List[SimplestEmployee]:
        return [rn.choice(available_hires)]


    
    