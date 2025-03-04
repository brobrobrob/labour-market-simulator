
from typing import Any, List, Sequence
from polars import DataFrame, datatypes as PlDtypes

from base_classes.base_employee import CURRENT_WAGE, EMPLOYEE_ID, EMPLOYEE_NAME, EMPLOYER_NAME, EMPLOYMENT_STATUS, PRODUCTIVITY, BaseEmployee
from base_classes.base_employer import CURRENT_EMPLOYEES, CURRENT_FUNDS, EMPLOYER_ID, INITIAL_FUNDS, IS_BANKRUPT, BaseEmployer
from functions.hire import hire
from scenarios.simplest import SimplestEmployee, SimplestEmployer

YEAR = 'year'
EMPLOYEE_DATA = 'EMPLOYEE_DATA'
EMPLOYER_DATA = 'EMPLOYER_DATA'

def record_state_in_tracker(tracker: dict[str, List[Any]], object: BaseEmployer | BaseEmployee) -> dict[str, List[Any]]:
    current_state = object.current_state()
    for key in current_state.keys():
        tracker[key] += [current_state[key]]
    return tracker

def simplest_simulate(number_of_years: int,
                      employees: Sequence[SimplestEmployee],
                      employers: Sequence[SimplestEmployer]):
    # Assign employees to employers, each employer in turn selecting employees based on their hiring policy.
    employers[0].choose_hires(available_hires=employees)
    while len(employees) != 0:
        for employer in employers:
            chosen_employees = employer.choose_hires(available_hires=employees)
            hire(employees=chosen_employees, employer=employer)
            employees = [employee for employee in employees if employee not in chosen_employees]
    # setup data schema
    employer_tracker = {
            YEAR: [],
            EMPLOYER_ID : [],
            EMPLOYER_NAME: [],
            INITIAL_FUNDS: [],
            CURRENT_FUNDS: [],
            CURRENT_EMPLOYEES: [],
            IS_BANKRUPT:[]
            }
    employee_tracker = {
                YEAR: [],
                EMPLOYEE_ID:[],
                EMPLOYER_ID: [],
                EMPLOYER_NAME: [],
                EMPLOYEE_NAME: [],
                EMPLOYMENT_STATUS: [],
                PRODUCTIVITY: [],
                CURRENT_WAGE:[]

    }
    year = 0
    while all([not employer.is_bankrupt for employer in employers]) and (year <= number_of_years):
        for employer in employers:
            record_state_in_tracker(tracker=employer_tracker, object=employer)
            employer.pay_employees()
            employer.current_funds = employer.current_funds + employer.annual_gross_income()
            employer_tracker[YEAR] += [year]
            for employee in employer.current_employees:
                record_state_in_tracker(tracker=employee_tracker, object=employee)
                employee_tracker[YEAR] += [year]
        year += 1
    return {
        EMPLOYEE_DATA: DataFrame(employee_tracker,
                                 schema={
                                    YEAR: PlDtypes.Int16,
                                    EMPLOYEE_ID: PlDtypes.String,
                                    EMPLOYER_ID: PlDtypes.String,
                                    EMPLOYER_NAME: PlDtypes.String,
                                    EMPLOYEE_NAME: PlDtypes.String,
                                    EMPLOYMENT_STATUS: PlDtypes.String,
                                    PRODUCTIVITY: PlDtypes.Int32,
                                    CURRENT_WAGE: PlDtypes.Int32,
                                    },
                                            strict=False),
        EMPLOYER_DATA: DataFrame(employer_tracker, 
                                 schema={
                                    YEAR: PlDtypes.Int16,
                                    EMPLOYER_ID: PlDtypes.String,
                                    EMPLOYER_NAME: PlDtypes.String,
                                    INITIAL_FUNDS: PlDtypes.Int32,
                                    CURRENT_FUNDS: PlDtypes.Int32,
                                    CURRENT_EMPLOYEES: PlDtypes.Struct(
                                        [
                                            PlDtypes.Field(name='employee_name', dtype=PlDtypes.String)
                                        ]
                                    ),
                                    IS_BANKRUPT: PlDtypes.Boolean},
                                    strict=False),

    }
