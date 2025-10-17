import subprocess
import sys
import os
import pytest
import re
from workInfo import *

def test_output(self):
    process = subprocess.run(
        ['python3','workPlanner.py'],
        captured_output = True,
        test = True,
        check = False
    )

    self.assertEqual(process.stdout.strip(), "What is your name: ")
    self.assertEqual(process.stdout.strip(), "How many hours will you work: ")
    self.assertEqual(process.stdout.strip(), "Enter the neighborhoods you want to work seperated by a space: : ")
    self.assertEqual(process.stdout.strip(), "Enter the days you want to work seperated by a space: ")
    self.assertEqual(process.stdout.strip(), "What is the fuel efficiency of your vehicle: ")
    self.assertEqual(process.stdout.strip(), "How many miles are you traveling: ")
    self.assertEqual(process.stdout.strip(), "What is the cost of fuel: ")
    self.assertEqual(process.stdout(), f"{name} is expected to make: ${value:.2f}")

def amountMadeFunc(base_pay, num_jobs_per_hr, hours, day_multiplier, neighborhood_multiplier):
    amountMade = base_pay * num_jobs_per_hr * hours * dayMultiplier * neighborhoodMultiplier
    return amountMade

def deductionFunc(milesTraveled, fuelEfficiency, costOfFuel):
    deduction = (milesTraveled / fuelEfficiency) * costOfFuel
    return deduction

def valueFunc(amountMade, deduction):
    value = amountMade - deduction
    return value

@pytest.mark.parametrize("input_a, input_b, input_c, input_d, input_e, expected_output", [
    (2, 3, 6),
    (5, 0, 0),
    (-2, 4, -8),
    (10, 10, 100),




