from __future__ import annotations
from typing import TYPE_CHECKING
from enum import Enum
if TYPE_CHECKING:
    from base_classes.base_employer import BaseEmployer

class EmploymentStatus(Enum):
    EMPLOYED = 'EMPLOYED'
    UNEMPLOYED = 'UNEMPLOYED'

class EmploymentInfo:
    def __init__(self,
                 employer: BaseEmployer | None):
        self.employer = employer
        self.employment_status = EmploymentStatus.EMPLOYED if employer is not None else EmploymentStatus.UNEMPLOYED



    