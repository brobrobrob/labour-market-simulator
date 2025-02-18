
from typing import List
from base_classes.base_employee import BaseEmployee, EmploymentStatus
from base_classes.base_employer import BaseEmployer


def hire(employees: List[BaseEmployee], employer: BaseEmployer):
    for employee in employees:
        if employee in employer.current_employees:
            raise ValueError(f'Employee: {employee.name}, id: {employee.id} is already employed by Company: {employer.name}, id {employer.id}')
        employee.employer = employer
        employee.employment_status = EmploymentStatus.EMPLOYED
    employer.current_employees = [*employer.current_employees, *employees]
    