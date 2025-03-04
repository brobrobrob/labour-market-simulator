
from abc import ABC, abstractmethod
from typing import Any, Dict, Sequence
import uuid
from matplotlib.colors import TABLEAU_COLORS
import base_classes.base_employee as BE
import random as rn

EMPLOYER_ID = 'employer_id'
EMPLOYER_NAME = 'employer_name'
INITIAL_FUNDS = 'initial_funds'
CURRENT_FUNDS = 'current_funds'
CURRENT_EMPLOYEES = 'current_employees'
IS_BANKRUPT = 'is_bankrupt'


class BaseEmployer(ABC):
    def __init__(self,
                 name: str,
                 initial_funds: int,
                 current_employees: Sequence[BE.BaseEmployee] = []):
        self.id: str = uuid.uuid4().hex
        self.name: str = name
        self.initial_funds: int = initial_funds
        self.current_funds: int = initial_funds
        self.current_employees: Sequence[BE.BaseEmployee] = current_employees
        self.is_bankrupt: bool = False

    def __eq__(self, other):
        if isinstance(other, BaseEmployer):
            return self.id == other.id
        else: return False

    
    @abstractmethod
    def annual_gross_income(self):
        pass

    @abstractmethod
    def calculate_wage(self, employee: BE.BaseEmployee):
        pass


    def declare_bankruptcy(self):
        self.is_bankrupt = True

    def pay_employees(self):
        for employee in self.current_employees:
            if employee.current_wage is None:
                raise ValueError(f'Employee: {employee.name}, {employee.id} has not had wage determined')
            if self.current_funds >= employee.current_wage:
                self.current_funds = self.current_funds - employee.current_wage
            else:
                self.declare_bankruptcy()

    def current_state(self) -> Dict[str, Any]:
        return {
            EMPLOYER_ID : self.id,
            EMPLOYER_NAME: self.name,
            INITIAL_FUNDS: self.initial_funds,
            CURRENT_FUNDS: self.current_funds,
            CURRENT_EMPLOYEES: {employee.name : employee.id for employee in self.current_employees},
            IS_BANKRUPT: self.is_bankrupt
        }




    

    