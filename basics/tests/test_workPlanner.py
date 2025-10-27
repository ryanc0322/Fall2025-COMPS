import subprocess
import sys
import os
import pytest
import re
import builtins
from solution_code.workInfo import checkList
from solution_code.workPlannerSolution import *


def _run_main_with_inputs(inputs):
    it = iter(inputs)
    monkey = lambda prompt='': next(it)
    # patch input
    builtins_input = builtins.input
    try:
        builtins.input = monkey
        # capture printed output
        from io import StringIO
        import sys
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            main()
        finally:
            out = sys.stdout.getvalue()
            sys.stdout = old_stdout
    finally:
        builtins.input = builtins_input
    return out


def test_main_valid_inputs():
    # Valid sequence of inputs that should produce a deterministic value
    inputs = [
        'Alex',      # name
        10,        # base_pay
        2,         # num_jobs_per_hr
        5,         # hours
        'A',         # neighborhoods
        'Monday',    # days
        25,        # fuelEfficiency
        100,       # milesTraveled
        3.5        # costOfFuel
    ]

    out = _run_main_with_inputs(inputs)
    expected_value = 10 * 2 * 5 * 1 * 1.05
    deduction = (100 / 25) * 3.5
    final = expected_value - deduction
    expected_line = f"Alex is expected to make: ${final:.2f}"
    assert expected_line in out




def test_amount_made_func_zero():
    result = amount_made_func(10, 2, 0, {'Monday':1}, {'A':1.05})
    assert result == 0

def test_deduction_precision():
    assert deduction_func(100, 25, 3.5) == pytest.approx((100/25) * 3.5)
    
def test_value_negative_deduction():
    # ensure value returned matches amount_made - deduction
    a = 200.0
    d = 250.0
    assert value_func(a, d) == pytest.approx(a - d)


@pytest.mark.parametrize(
    "base_pay",
    [2,6.5,11,19,36.5,50]
)

@pytest.mark.parametrize(
    "num_jobs_per_hr",
    [1,2,3,5,7,20]
)

@pytest.mark.parametrize(
    "hours",
    [5,20,12,40,36.5,80,76]
)

@pytest.mark.parametrize(
    "day_multiplier",
    [
        {'Monday' : 1},
        {'Tuesday' : 1.05},
        {'Wednesday' : 1},
        {'Thursday' : 1},
        {'Friday' : 1.1},
        {'Saturday' : 1.4},
        {'Sunday' : 1.4}
    ]
)

@pytest.mark.parametrize(
    "neighborhood_multiplier",
    [
        {'A': 1.05},
        {'B': 1.1},
        {'C': 1.08},
        {'D': 1.07}
    ]
)


def test_amount_made_func(base_pay, num_jobs_per_hr, hours, neighborhood_multiplier, day_multiplier):
    """Test calculate_total by stacking parametrizations."""
    result = amount_made_func(base_pay, num_jobs_per_hr, hours, neighborhood_multiplier, day_multiplier)

    # Assert logic for combinations
    if 'A' in neighborhood_multiplier:
        if 'Sunday' in day_multiplier:
            expected = base_pay * num_jobs_per_hr * hours * 1.05 * 1.4
        elif 'Monday' in day_multiplier:
            expected = base_pay * num_jobs_per_hr * hours * 1.05 * 1
        elif 'Tuesday' in day_multiplier:
            expected = base_pay * num_jobs_per_hr * hours * 1.05 * 1.05
        elif 'Wednesday' in day_multiplier:
            expected = base_pay * num_jobs_per_hr * hours * 1.05 * 1
        elif 'Thursday' in day_multiplier:
            expected = base_pay * num_jobs_per_hr * hours * 1.05 * 1
        elif 'Friday' in day_multiplier:
            expected = base_pay * num_jobs_per_hr * hours * 1.05 * 1.1
        elif 'Saturday' in day_multiplier:
            expected = base_pay * num_jobs_per_hr * hours * 1.05 * 1.4
    if 'B' in neighborhood_multiplier:
        if 'Sunday' in day_multiplier:
            expected = base_pay * num_jobs_per_hr * hours * 1.1 * 1.4
        elif 'Monday' in day_multiplier:
            expected = base_pay * num_jobs_per_hr * hours * 1.1 * 1
        elif 'Tuesday' in day_multiplier:
            expected = base_pay * num_jobs_per_hr * hours * 1.1 * 1.05
        elif 'Wednesday' in day_multiplier:
            expected = base_pay * num_jobs_per_hr * hours * 1.1 * 1
        elif 'Thursday' in day_multiplier:
            expected = base_pay * num_jobs_per_hr * hours * 1.1 * 1
        elif 'Friday' in day_multiplier:
            expected = base_pay * num_jobs_per_hr * hours * 1.1 * 1.1
        elif 'Saturday' in day_multiplier:
            expected = base_pay * num_jobs_per_hr * hours * 1.1 * 1.4
    if 'C' in neighborhood_multiplier:
        if 'Sunday' in day_multiplier:
            expected = base_pay * num_jobs_per_hr * hours * 1.08 * 1.4
        elif 'Monday' in day_multiplier:
            expected = base_pay * num_jobs_per_hr * hours * 1.08 * 1
        elif 'Tuesday' in day_multiplier:
            expected = base_pay * num_jobs_per_hr * hours * 1.08 * 1.05
        elif 'Wednesday' in day_multiplier:
            expected = base_pay * num_jobs_per_hr * hours * 1.08 * 1
        elif 'Thursday' in day_multiplier:
            expected = base_pay * num_jobs_per_hr * hours * 1.08 * 1
        elif 'Friday' in day_multiplier:
            expected = base_pay * num_jobs_per_hr * hours * 1.08 * 1.1
        elif 'Saturday' in day_multiplier:
            expected = base_pay * num_jobs_per_hr * hours * 1.08 * 1.4
    if 'D' in neighborhood_multiplier:
        if 'Sunday' in day_multiplier:
            expected = base_pay * num_jobs_per_hr * hours * 1.07 * 1.4
        elif 'Monday' in day_multiplier:
            expected = base_pay * num_jobs_per_hr * hours * 1.07 * 1
        elif 'Tuesday' in day_multiplier:
            expected = base_pay * num_jobs_per_hr * hours * 1.07 * 1.05
        elif 'Wednesday' in day_multiplier:
            expected = base_pay * num_jobs_per_hr * hours * 1.07 * 1
        elif 'Thursday' in day_multiplier:
            expected = base_pay * num_jobs_per_hr * hours * 1.07 * 1
        elif 'Friday' in day_multiplier:
            expected = base_pay * num_jobs_per_hr * hours * 1.07 * 1.1
        elif 'Saturday' in day_multiplier:
            expected = base_pay * num_jobs_per_hr * hours * 1.07 * 1.4

        
    assert result == expected

@pytest.mark.parametrize(
    "miles_traveled",
    [2,6.5,11,19,36.5,50]
)

@pytest.mark.parametrize(
    "fuel_efficiency",
    [2,6.5,11,19,36.5,50]
)

@pytest.mark.parametrize(
    "cost_of_fuel",
    [2,6.5,11,19,36.5,50]
)

def test_deduction_func(miles_traveled, fuel_efficiency, cost_of_fuel):
    result = deduction_func(miles_traveled, fuel_efficiency, cost_of_fuel)
    expected = (miles_traveled / fuel_efficiency) * cost_of_fuel

    assert result == expected

@pytest.mark.parametrize(
    "amount_made",
    [2,6.5,11,19,36.5,50]
)

@pytest.mark.parametrize(
    "deduction",
    [2,6.5,11,19,36.5,50]
)

def test_value_func(amount_made, deduction):
    result = value_func(amount_made, deduction)
    expected = amount_made - deduction

    assert result == expected

def test_pylint_student_code():
    result = subprocess.run(
        ["pylint", "--rcfile=.pylintrc", "solution.py"],
        capture_output=True,
        text=True
    )

    print("\n")
    print("--- PYLINT ANALYSIS START ---")
    print(result.stdout)
    print("--- PYLINT ANALYSIS END ---")

    # find pylint score from the ouput
    match = re.search(r"rated at ([\d\.]+)/10", result.stdout)
    if not match:
        pytest.fail("Error: No pylint score found.")

    score = float(match.group(1))

    # Fail the test if score < 8.0
    assert score >= 8.0, f"Pylint score too low: {score}/10"
