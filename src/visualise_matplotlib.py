from typing import Dict
from matplotlib.colors import TABLEAU_COLORS
from matplotlib.typing import ColourType
import polars as pl
from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
import random as rn

from functions.simulate import simplest_simulate
from scenarios.generous_frugal_fair import FairSimpleEmployer, FrugalSimpleEmployer, GenerousSimpleEmployer
from scenarios.simplest import SimplestEmployee

def select_single_employer(df : pl.DataFrame, employer_name: str) -> pl.DataFrame:
    return df.filter(pl.col('employer_name') == employer_name)

def select_single_employee(df : pl.DataFrame, employee_name: str) -> pl.DataFrame:
    return df.filter(pl.col('employee_name') == employee_name)

def visualise_matplotlib(data: Dict[str, pl.DataFrame], employer_names: list[str], employee_names: list[str]):
    fig, (ax1, ax2) = plt.subplots(1, 2)
    year = 'year'
    current_funds = 'current_funds'
    current_wage = 'current_wage'
    # Assign each employer a colour for consistency across plots
    employer_colour_mapping = {
          employer_name: list(TABLEAU_COLORS.values())[i] for i, employer_name in enumerate(employer_names)
    }
    plot_employers_funds_over_time(data=data['EMPLOYER_DATA'],
                                   ax=ax1,
                                   fig=fig,
                                   year_col_name=year,
                                   current_funds_col_name=current_funds,
                                   employer_colour_mapping=employer_colour_mapping)
    plot_employees_current_wages_over_time(data=data['EMPLOYEE_DATA'],
                                          ax=ax2,
                                          fig=fig,
                                          year_col_name=year,
                                          current_wage_col_name=current_wage,
                                          employer_colour_mapping=employer_colour_mapping)
    plt.show()

def plot_employers_funds_over_time(data: pl.DataFrame,
                                   ax: Axes,
                                   fig: Figure,
                                   year_col_name: str,
                                   current_funds_col_name: str,
                                   employer_colour_mapping: Dict[str, ColourType]):
    for employer_name, employer_colour in employer_colour_mapping.items():
        employer_df = select_single_employer(data, employer_name)
        ax.plot(employer_df[year_col_name], employer_df[current_funds_col_name], label=employer_name, color=employer_colour)
    fig.legend(loc='upper left')
    ax.set_xlabel('Year')
    ax.set_ylabel('Employer Funds')
    ax.set_xticks(range(0, 11))
    ax.set_title('Employer funds over time')
    ax.set_xlim(0, float(data[year_col_name].max()))

def plot_employees_current_wages_over_time(data: pl.DataFrame,
                                           ax: Axes,
                                           fig: Figure,
                                           year_col_name: str,
                                           current_wage_col_name: str,
                                           employer_colour_mapping: Dict[str, ColourType]):
    print(data.columns)
    for employee in data['employee_name'].unique().to_list():
        employee_df = select_single_employee(data, employee)
        ax.plot(employee_df[year_col_name], employee_df[current_wage_col_name], label=employee, color=employer_colour_mapping[employee_df['employer_name'][0]])

          
        
    ax.set_xlabel('Year')
    ax.set_ylabel('Employee Wages')
    ax.set_xticks(range(0, 11))
    ax.set_title('Employee wages over time')
    ax.set_xlim(0, float(data['year'].max()))

def main():
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
    visualise_matplotlib(data=result,
                         employer_names=['Frugal Ltd.', 'Fair Ltd.', 'Generous Ltd.'],
                            employee_names=['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'])
                         
                         

if __name__ == '__main__':
    main()