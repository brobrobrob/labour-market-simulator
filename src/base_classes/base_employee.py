from __future__ import annotations
from abc import ABC
from typing import Any, Dict
import uuid

from base_classes.employment_info import EmploymentInfo, EmploymentStatus

EMPLOYEE_NAME = 'employee_name'
EMPLOYER_NAME = 'employer_name'
EMPLOYMENT_STATUS = 'employment_status'
PRODUCTIVITY = 'productivity'
CURRENT_WAGE = 'current_wage'
EMPLOYEE_ID = 'employee_id'
EMPLOYER_ID = 'employer_id'
    
class BaseEmployee(ABC):
    def __init__(self,
                 name: str,
                 productivity: int
                 ):
        self.id: str = uuid.uuid4().hex
        self.name: str = name
        self.productivity: int = productivity
        self.employment_info: EmploymentInfo = EmploymentInfo(employer=None)
        self.current_wage: int | None = None

    def __eq__(self, other):
        if isinstance(other, BaseEmployee):
            return self.id == other.id
        else: return False

    def current_state(self) -> Dict[str, Any]:
        if self.employment_info.employment_status == EmploymentStatus.EMPLOYED:
            return {
                EMPLOYEE_ID: self.id,
                EMPLOYEE_NAME: self.name,
                EMPLOYER_NAME: self.employment_info.employer.name,
                EMPLOYER_ID: self.employment_info.employer.id,
                EMPLOYMENT_STATUS: EmploymentStatus.EMPLOYED,
                CURRENT_WAGE: self.current_wage,
                PRODUCTIVITY: self.productivity
            }
        if self.employment_info.employment_status == EmploymentStatus.UNEMPLOYED:
            return {
                EMPLOYEE_ID: self.id,
                EMPLOYEE_NAME: self.name,
                EMPLOYER_NAME: None,
                EMPLOYER_ID: None,
                EMPLOYMENT_STATUS: EmploymentStatus.UNEMPLOYED,
                CURRENT_WAGE: 0,
                PRODUCTIVITY: self.productivity
            }
        else:
            raise ValueError('Unhandled employment status')



    