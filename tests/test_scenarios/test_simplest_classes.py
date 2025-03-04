
from base_classes.base_employee import EmploymentInfo, EmploymentStatus
from functions.hire import hire
from scenarios.simplest import SimplestEmployee, SimplestEmployer

class TestSimplesEmployer:
    def test_annual_gross_income_and_calculate_wage(self):
        uut = SimplestEmployer(name='Hideout Cafe', initial_funds=5)
        waitress_1 = SimplestEmployee(name='Cassie', productivity=30000)
        waitress_2 = SimplestEmployee(name='Agnes', productivity=35000)
        hire(employees=[waitress_1, waitress_2], employer=uut)
        assert uut.annual_gross_income() == 65000
        assert uut.calculate_wage(employee=waitress_1) == 30000

    def test_choose_hires(self):
        uut = SimplestEmployer(name='Dill Cafe', initial_funds=6)
        waitress_1 = SimplestEmployee(name='Cassie', productivity=30000)
        waitress_2 = SimplestEmployee(name='Agnes', productivity=35000)
        waitress_3 = SimplestEmployee(name='Maggie', productivity=40000)
        result = uut.choose_hires(available_hires=[waitress_1, waitress_2, waitress_3])
        assert any([employee in result for employee in [waitress_1, waitress_2, waitress_3]])
        assert len(result) == 1


