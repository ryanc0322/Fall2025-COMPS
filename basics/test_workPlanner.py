import subprocess
import sys
import os
import pytest
import re
from workPlanner2 import amountMadeFunc
from workPlanner2 import deductionFunc
from workPlanner2 import valueFunc


def checkList(givenList)  :
    total = 1
    if not givenList :
        raise ValueError("There are no entries in the given list.  \nPlease check both your neighborhoods and your days lists and make sure that there are values there that correspond to what the list is looking for.")
    seen = set()
    first = givenList[0]
    if first in dayParams.multipliers :
        for item in givenList :
            if item in seen :
                raise ValueError("There is a duplicate day in your list of days.  \nMake sure there is only one of each of the days you are selecting")
            elif item in dayParams.multipliers:
                seen.add(item)
                total = total * dayParams.multipliers[item]
            else :
                 raise ValueError("You have entered something invalid to your days list.  \nPlease check to make sure there are only either 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', or 'Sunday' in your list.")

    elif first in neighborhoodParams.multipliers :
        for item in givenList :
            if item in seen :
                raise ValueError("There is a duplicate neighborhood in your list of days.  \nMake sure there is only one of each of the neighborhoods you are selecting")
            elif item in neighborhoodParams.multipliers:
                seen.add(item)
                total = total * neighborhoodParams.multipliers[item]
            else:
                raise ValueError("You have entered something invalid to your neighborhoods list.  \nPlease check to make sure there are only either 'A', 'B', 'C', or 'D' in your list.")
    else :
        raise ValueError("You have entered something into the list that is not a valid day or neighborhood.\nPlease check both your neighborhoods and you days lists and make sure that you only have either 'A', 'B', 'C', or 'D' in the neighborhoods list \nand 'Monday', 'Tuesday', 'Wednesday', 'Thursday', or 'Friday' in the days list.")
    return total


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





