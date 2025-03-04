
from base_classes.base_employee import BaseEmployee, EmploymentInfo, EmploymentStatus
from base_classes.base_employer import BaseEmployer
from functions.hire import hire

class SimplestEmployee(BaseEmployee):
    pass

class SimplestEmployer(BaseEmployer):
    def annual_gross_income(self) -> int:
        return 10000000
    
    def calculate_wage(self, employee: BaseEmployee):
        return 50000

class TestBaseEmployer:
    def test_init(self):
        uut = SimplestEmployer(initial_funds=500000, name='McDonalds')
        assert uut.current_employees == []
        assert uut.current_funds == 500000
        assert uut.initial_funds == 500000
        assert not uut.is_bankrupt
    
    def test_equality(self):
        uut_1 = SimplestEmployer(name='Tesco', initial_funds=120000)
        uut_2 = SimplestEmployer(name='Tesco_2', initial_funds=120000)
        assert uut_1 != uut_2
        assert uut_1 == uut_1
        assert uut_2 != 'Anything else'

    def test_declare_bankruptcy(self):
        uut = SimplestEmployer(initial_funds=1000000000, name = 'WeWork')
        uut.declare_bankruptcy()
        assert uut.is_bankrupt
    
    def test_current_state(self):
        uut = SimplestEmployer(initial_funds=1200000, name = 'Springfield Nuclear Power Plant')
        homer = SimplestEmployee('Homer Simpson', productivity=10)
        lenny = SimplestEmployee('Lenny Leonard', productivity=100000)
        hire(employees=[homer, lenny], employer=uut)
        result = uut.current_state()

        assert result['initial_funds']==1200000
        assert result['current_funds']==1200000
        assert result['employer_id'] is not None
        assert all([employee in result['current_employees'].keys() for employee in ['Homer Simpson', 'Lenny Leonard']])
        assert not result['is_bankrupt']

    def test_pay_employees(self):
        uut = SimplestEmployer(initial_funds=100001, name='Duff Beer')
        barney = SimplestEmployee('Barney Gumble', productivity=10000)
        hire(employees=[barney], employer=uut)
        uut.pay_employees()
        assert uut.current_funds == 50001
        assert not uut.is_bankrupt
        uut.pay_employees()
        assert uut.current_funds == 1
        assert  not uut.is_bankrupt
        uut.pay_employees()
        assert uut.is_bankrupt


class TestEmploymentInfo:
    def test_init(self):
        audi = SimplestEmployer('Audi Ltd', initial_funds=200000)
        uut = EmploymentInfo(audi)
        assert uut.employment_status == EmploymentStatus.EMPLOYED
        assert uut.employer.name == 'Audi Ltd'

class TestBaseEmployee:
    def test_init(self):
        uut = SimplestEmployee(name='Bob', productivity=100000)
        assert uut.name == 'Bob'
        assert uut.productivity == 100000
        assert uut.id is not None
        assert uut.employment_info is not None
    
    def test_equality(self):
        uut_1 = SimplestEmployee(name='Samantha', productivity=120000)
        uut_2 = SimplestEmployee(name='Samantha', productivity=120000)
        assert uut_1 != uut_2
        assert uut_1 == uut_1
        assert uut_2 != 'Anything else'
    
    def test_current_state(self):
        uut = SimplestEmployee(name='Hank', productivity=60000)
        bbc = SimplestEmployer(name='British Broadcasting', initial_funds=70000)
        hire(employees=[uut], employer=bbc)
        result = uut.current_state()
        assert result['productivity'] == 60000
        assert result['current_wage'] == 50000
        assert result['employee_name'] == 'Hank'
        assert result['employer_name'] == 'British Broadcasting'
        assert result['employment_status'] == EmploymentStatus.EMPLOYED
        assert result['employee_id'] is not None
        assert result['employer_id'] is not None
        # If more keys are added to this, update the test
        assert len(result.keys()) == 7
    
    def test_current_state_when_unemployed(self):
        uut = SimplestEmployee(name='Walter', productivity=45000)
        result = uut.current_state()
        assert result['productivity'] == 45000
        assert result['current_wage'] == 0
        assert result['employee_name'] == 'Walter'
        assert result['employer_name'] is None
        assert result['employment_status'] == EmploymentStatus.UNEMPLOYED
        assert result['employee_id'] is not None
        assert result['employer_id'] is None
        # If more keys are added to this, update the test
        assert len(result.keys()) == 7