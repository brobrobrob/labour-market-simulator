
from typing import Sequence
from base_classes.base_employee import BaseEmployee, EmploymentInfo
from base_classes.base_employer import BaseEmployer


def hire(employees: Sequence[BaseEmployee], employer: BaseEmployer):
    for i, employee in enumerate(employees):
        if employee in employer.current_employees:
            raise ValueError(f'Employee: {employee.name}, id: {employee.id} is already employed by Company: {employer.name}, id {employer.id}')
        employees[i].employment_info = EmploymentInfo(employer=employer)
        employees[i].current_wage = employer.calculate_wage(employee)
    employer.current_employees = [*employer.current_employees, *employees]
    