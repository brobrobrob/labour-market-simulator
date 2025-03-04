

import pytest
from base_classes.base_employee import EmploymentStatus
from functions.hire import hire
from tests.test_base_classes.test_base_classes import SimplestEmployee, SimplestEmployer


def test_whenHireCalled_thenUpdatesObjectsState():
    test_employer = SimplestEmployer(name='civil_service', initial_funds=0)
    test_employee = SimplestEmployee(name='Kat', productivity=40000)
    hire(employees=[test_employee], employer=test_employer)
    assert test_employee.employment_info.employment_status == EmploymentStatus.EMPLOYED
    assert test_employee.employment_info.employer == test_employer
    assert test_employee in test_employer.current_employees

def test_whenAlreadyHired_thenErrorsAsExpected():
    test_employee = SimplestEmployee(name='Kit', productivity=45000)
    test_employer = SimplestEmployer(name='Hampshire County Council', initial_funds=10000, current_employees=[test_employee])
    with pytest.raises(ValueError):
        hire(employees=[test_employee], employer=test_employer)
    
