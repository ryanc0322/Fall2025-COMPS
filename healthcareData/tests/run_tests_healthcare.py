"""
Ryan Choi
Description: Script to test healthcareData_student and solution_code
using Pytest and Pylint. Results written to a text file.
"""

import subprocess

pytest_command = ["python", "-m", "pytest", "-v", "test_healthcare.py"]
pylint_command = ["python", "-m", "pylint", "--rcfile=.pylintrc", "../solution_code/solution.py"]

run_pytest = subprocess.run(pytest_command, capture_output=True, text=True)
run_pylint = subprocess.run(pylint_command, capture_output=True, text=True)

file = "test_results_healthcare.txt"

with open(file, "w", encoding="utf-8") as f:
    f.write("Test Functions (Pytest)\n\n")
    f.write(run_pytest.stdout)
    f.write("\n\nTest Style (Pylint)\n\n")
    f.write(run_pylint.stdout)
    f.write("\n")

print("Testing complete.")
print(f"Results written to: {file}")