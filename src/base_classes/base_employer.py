
from typing import List

from base_classes.base_employee import BaseEmployee


class BaseEmployer:
    def __init__(self,
                 initial_funds: int,
                 current_employees: List[BaseEmployee] = []
                 ):
        self.initial_funds: int = initial_funds
        self.current_funds: int = initial_funds
        self.current_employees: List[BaseEmployee] = current_employees

    

    