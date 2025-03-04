

from functions.simulate import simplest_simulate
from scenarios.simplest import SimplestEmployee, SimplestEmployer
from polars import DataFrame
from polars.testing import assert_frame_equal
import polars.datatypes as PlTypes

def test_whenSimulateCalledwithOneEmployerAndOneEmployee_thenProducesExpectedResult():
    single_employer = SimplestEmployer(name ='Diddly Squat Farm', initial_funds=100000)
    single_employee = SimplestEmployee(name = 'Jeremy Clarkson', productivity=10000)
    result = simplest_simulate(number_of_years=3,
                               employees=[single_employee],
                               employers=[single_employer])
    expected_employer_data = DataFrame({
        'employer_name' : ['Diddly Squat Farm'] * 4 ,
        'year' : [0, 1, 2 ,3],
        'employer_id': [single_employer.id] * 4,
        'initial_funds': [100000] * 4,
        'current_funds': [100000] * 4,
        'current_employees': [{'Jeremy Clarkson': single_employee.id}]* 4,
        'is_bankrupt': [False] * 4

    },
    schema={
        'employer_name' : PlTypes.String ,
        'year' : PlTypes.Int16,
        'employer_id': PlTypes.String,
        'initial_funds': PlTypes.Int32,
        'current_funds': PlTypes.Int32,
        'current_employees': PlTypes.Struct([PlTypes.Field(name='employee_name', dtype=PlTypes.String)]),
        'is_bankrupt': PlTypes.Boolean
    })
    assert_frame_equal(result['EMPLOYER_DATA'], expected_employer_data, check_column_order=False)
