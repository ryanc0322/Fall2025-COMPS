import subprocess
import sys
import os
import pytest
import re
from workInfo import checkList
from workPlanner2 import amountMadeFunc, deductionFunc, valueFunc

def test_amountMade_zero():
    result = amountMadeFunc(10, 2, 0, {'Monday':1}, {'A':1.05})
    assert result == 0

def test_deduction_precision():
    assert deductionFunc(100, 25, 3.5) == pytest.approx((100/25) * 3.5)

def test_value_negative_deduction():
    # ensure value returned matches amountMade - deduction
    a = 200.0
    d = 250.0
    assert valueFunc(a, d) == pytest.approx(a - d)


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


def test_amountMadeFunc(base_pay, num_jobs_per_hr, hours, neighborhood_multiplier, day_multiplier):
    """Test calculate_total by stacking parametrizations."""
    result = amountMadeFunc(base_pay, num_jobs_per_hr, hours, neighborhood_multiplier, day_multiplier)

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
    "milesTraveled",
    [2,6.5,11,19,36.5,50]
)

@pytest.mark.parametrize(
    "fuelEfficiency",
    [2,6.5,11,19,36.5,50]
)

@pytest.mark.parametrize(
    "costOfFuel",
    [2,6.5,11,19,36.5,50]
)

def test_deductionFunc(milesTraveled, fuelEfficiency, costOfFuel):
    result = deductionFunc(milesTraveled, fuelEfficiency, costOfFuel)
    expected = (milesTraveled / fuelEfficiency) * costOfFuel
    
    assert result == expected

@pytest.mark.parametrize(
    "amountMade",
    [2,6.5,11,19,36.5,50]
)

@pytest.mark.parametrize(
    "deduction",
    [2,6.5,11,19,36.5,50]
)

def test_valueFunc(amountMade, deduction):
    result = valueFunc(amountMade, deduction)
    expected = amountMade - deduction

    assert result == expected





