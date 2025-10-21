"""
run_tests.py

Chloe Simanek

Description: Script to test shopping_simulator functions
using Pytest and Pylint. Results written to a text file. 
"""

import subprocess

pytest_command = ["python", "-m", "pytest", "-v"]
pylint_command = ["python", "-m", "pylint", "--rcfile=tests/.pylintrc", "shopping_simulator_solution.py"]

run_pytest = subprocess.run(pytest_command, capture_output=True, text=True)
run_pylint = subprocess.run(pylint_command, capture_output=True, text=True)

file = "test_results.txt"

with open("test_results.txt", "w", encoding="utf-8") as f:
    f.write("PYTEST RESULTS \n\n")
    f.write(run_pytest.stdout)
    f.write("\n\nPYLINT RESULTS \n")
    f.write(run_pylint.stdout)
    f.write("\n")

print("Testing complete")
print(f"Results written to: {file}")