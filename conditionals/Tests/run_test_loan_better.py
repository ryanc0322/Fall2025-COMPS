"""
Description: Script to test loanApproval_better.py and and the test file
using Pytest and Pylint. Results written to a text file.
"""

import subprocess

pytest_command = ["python", "-m", "pytest", "-v", "test_loan_better.py"]
pylint_command = ["python", "-m", "pylint", "--rcfile=.pylintrc", "../ProductionCode/loanApproval_better.py"]

run_pytest = subprocess.run(pytest_command, capture_output=True, text=True)
run_pylint = subprocess.run(pylint_command, capture_output=True, text=True)

file = "test_results_loan_better.txt"

with open(file, "w", encoding="utf-8") as f:
    f.write("Test Functions (Pytest)\n\n")
    f.write(run_pytest.stdout)
    f.write("\n\nTest Style (Pylint)\n\n")
    f.write(run_pylint.stdout)
    f.write("\n")

print("Testing complete.")
print(f"Results written to: {file}")
