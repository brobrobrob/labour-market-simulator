
from abc import ABC, abstractmethod
from typing import List
import uuid

import base_classes.base_employee as BE


class BaseEmployer(ABC):
    def __init__(self,
                 name: str,
                 initial_funds: int,
                 current_employees: List[BE.BaseEmployee] = []
                 ):
        self.id: uuid.UUID = uuid.uuid4()
        self.name: str = name
        self.initial_funds: int = initial_funds
        self.current_funds: int = initial_funds
        self.current_employees: List[BE.BaseEmployee] = current_employees
    
    @abstractmethod
    def annual_revenue():
        pass



    

    