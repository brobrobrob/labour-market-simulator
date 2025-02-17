
from base_classes.base_employee import BaseEmployee
from base_classes.base_employer import BaseEmployer


class TestBaseEmployer:
    def test_init(self):
        uut = BaseEmployer(initial_funds=500000)
        assert uut.current_employees == []
        assert uut.current_funds == 500000
        assert uut.initial_funds == 500000

class TestBaseEmployee:
    def test_init(self):
        uut = BaseEmployee(name='Bob', productivity=100000)
        assert uut.name == 'Bob'
        assert uut.productivity == 100000
        assert uut.id is not None
    
    def test_equality(self):
        class TestEmployee(BaseEmployee):
            pass
        uut_1 = TestEmployee(name='Samantha', productivity=120000)
        uut_2 = TestEmployee(name='Samantha', productivity=120000)
        assert uut_1 != uut_2
        assert uut_1 == uut_1
        assert uut_2 != 'Anything else'