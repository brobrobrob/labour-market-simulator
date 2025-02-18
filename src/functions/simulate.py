
from typing import List

from base_classes.base_employee import BaseEmployee
from base_classes.base_employer import BaseEmployer
from functions import hire


def simulate(start_year: int, 
             number_of_years: int,
             employees: List[BaseEmployee],
             employers: List[BaseEmployer]):
    for employer in employers:
        hire()
