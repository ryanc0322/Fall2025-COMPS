import subprocess
import sys
import os
import pytest
import re


@pytest.fixture(scope="session")
def captured_sections():
    """
    Run student's healthcare.py (or solution.py) without showing Matplotlib pop-ups.
    Capture the printed output and split by section markers like 'Answer to ...' for easier comparisons
    """
    env = os.environ.copy()
    env["MPLBACKEND"] = "Agg"  # Disable visualization popups from matplotlib

    result = subprocess.run(
        [sys.executable, "solution.py"],  # or "healthcare.py" for student submission. this should be the code you want to test
        capture_output=True,
        text=True,
        cwd=os.path.join(os.path.dirname(__file__), "../solution_code"), 
        env=env
    )


    assert result.returncode == 0, (
        f"Script exited with code {result.returncode}\n\nSTDERR:\n{result.stderr}"
    )

    # Clean the output
    full_output = result.stdout.strip()

    # Split into parts using section markers
    # Each marker starts with "Answer to"
    parts = re.split(r"Answer to (.+?) goes here", full_output)

    # Convert into a dictionary for easier test checking process
    section_outputs = {}
    for i in range(1, len(parts) - 1, 2):
        label = parts[i].strip()
        output = parts[i + 1].strip()
        section_outputs[label] = output

    return section_outputs


def test_part1_data_loading(captured_sections):
    """Check Part 1: first row, first five conditions, and number of patients."""
    expected_output = """Bobby JacksOn 30 Male B- Cancer 2024-01-31 Matthew Smith Northview Medical Urgent 2024-02-02 Paracetamol Normal
Cancer
Obesity
Obesity
Diabetes
Cancer
55500""".strip()

    assert captured_sections["Print the first row"] == expected_output, (
        f"\nEXPECTED (Part 1):\n{expected_output}\n\nGOT:\n{captured_sections['Print the first row']}"
    )


def test_part2_demographics(captured_sections):
    """Check printed age and gender distribution percentages."""
    expected_output = """Under 18: 0.21%
18-30: 17.26%
30-50: 29.39%
50-70: 29.78%
Over 70: 23.37%
Percentage of female patients: 49.96%
Percentage of male patients: 50.04%""".strip()

    assert captured_sections["Demographics"] == expected_output, (
        f"\nEXPECTED (Part 2):\n{expected_output}\n\nGOT:\n{captured_sections['Demographics']}"
    )


def test_part3_hospital_representation(captured_sections):
    """Check printed hospital representation percentages."""
    expected_output = """Northview Medical: 18.02%
Riverside Clinic: 12.61%
Henderson-Johnson Hospital: 27.03%
Greenfield Health: 32.43%
Summit Regional: 9.91%""".strip()

    assert captured_sections["Hospital representation"] == expected_output, (
        f"\nEXPECTED (Part 3):\n{expected_output}\n\nGOT:\n{captured_sections['Hospital representation']}"
    )