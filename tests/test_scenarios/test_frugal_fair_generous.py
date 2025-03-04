
from functions.simulate import simplest_simulate
from scenarios.generous_frugal_fair import FairSimpleEmployer, FrugalSimpleEmployer, GenerousSimpleEmployer
from scenarios.simplest import SimplestEmployee
import polars as pl
from polars.testing import assert_series_equal

class TestSimplesEmployer:
    def test_simulation(self):
        frugal = FrugalSimpleEmployer(name='Frugal Ltd.', initial_funds=100000)
        fair = FairSimpleEmployer(name='Fair Ltd.', initial_funds=100000)
        generous = GenerousSimpleEmployer(name='Generous Ltd.', initial_funds=100000)

        employees = [
            SimplestEmployee(name='Alice', productivity=10000),
            SimplestEmployee(name='Bob', productivity=20000),
            SimplestEmployee(name='Charlie', productivity=30000),
            SimplestEmployee(name='David', productivity=40000),
            SimplestEmployee(name='Eve', productivity=50000),
            SimplestEmployee(name='Frank', productivity=60000)
        ]

        result = simplest_simulate(number_of_years=10,
                                   employees=employees,
                                   employers=[frugal, fair, generous])
        assert len(frugal.current_employees) == 2
        assert len(fair.current_employees) == 2
        assert len(generous.current_employees) == 2

        assert len(result['EMPLOYER_DATA']) <= 33
        assert len(result['EMPLOYEE_DATA']) <= 66

        year_0_df = result['EMPLOYER_DATA'].filter(pl.col('year') == pl.lit(0))
        assert year_0_df.schema == pl.Schema({
            'year': pl.Int16,
            'employer_id': pl.String,
            'employer_name': pl.String,
            'initial_funds': pl.Int32,
            'current_funds': pl.Int32,
            'current_employees': pl.Struct([pl.Field(name='employee_name', dtype=pl.String)]),
             'is_bankrupt': pl.Boolean
        })
        assert_series_equal(year_0_df['current_funds'], pl.Series(name='current_funds', values=[100000]*3, dtype=pl.Int32))
                                                   





