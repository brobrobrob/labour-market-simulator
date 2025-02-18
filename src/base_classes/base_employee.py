from abc import ABC
import uuid

import base_classes.employment_info as EmployInfo

class BaseEmployee(ABC):
    def __init__(self,
                 name: str,
                 productivity: int
                 ):
        self.id: uuid.UUID = uuid.uuid4()
        self.name: str = name
        self.productivity: int = productivity
        self.employment_info: EmployInfo.EmploymentInfo = EmployInfo.EmploymentInfo(employer=None)

    def __eq__(self, other):
        if isinstance(other, BaseEmployee):
            return self.id == other.id
        else: return False



    