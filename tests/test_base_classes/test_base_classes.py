
from base_classes.base_employee import BaseEmployee
from base_classes.base_employer import BaseEmployer

class FakeEmployee(BaseEmployee):
    pass

class FakeEmployer(BaseEmployer):
    def annual_revenue(self) -> int:
        return 10000000

class TestBaseEmployer:
    def test_init(self):
        uut = FakeEmployer(initial_funds=500000, name='McDonalds')
        assert uut.current_employees == []
        assert uut.current_funds == 500000
        assert uut.initial_funds == 500000

class TestBaseEmployee:
    def test_init(self):
        uut = FakeEmployee(name='Bob', productivity=100000)
        assert uut.name == 'Bob'
        assert uut.productivity == 100000
        assert uut.id is not None
    
    def test_equality(self):
        uut_1 = FakeEmployee(name='Samantha', productivity=120000)
        uut_2 = FakeEmployee(name='Samantha', productivity=120000)
        assert uut_1 != uut_2
        assert uut_1 == uut_1
        assert uut_2 != 'Anything else'

    # def test_hiring()