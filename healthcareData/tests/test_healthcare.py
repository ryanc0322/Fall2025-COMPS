import subprocess
import sys
import os
import pytest
import re


@pytest.fixture(scope="session")
def captured_sections():
    """
    Run code and captures answer excluding the matplotlib graphs.
    Capture the output to account for some flexibility in formats.
    """
    env = os.environ.copy()
    env["MPLBACKEND"] = "Agg"  # Disable visualization popups from matplotlib

    result = subprocess.run(
        [sys.executable, "solution.py"],  # or "healthcare.py" for student submission. this should be what you want to test
        capture_output=True,
        text=True,
        cwd=os.path.join(os.path.dirname(__file__), "../solution_code"), 
        env=env
    )


    assert result.returncode == 0, (
        f"Script exited with code {result.returncode}\n\nSTDERR:\n{result.stderr}"
    )

    # process the output to be clean
    full_output = result.stdout.strip()

    # split the output by "Answer to ... goes here"
    parts = re.split(r"Answer to (.+?) goes here", full_output)

    # convert into a dictionary for test checking process
    section_outputs = {}
    for i in range(1, len(parts) - 1, 2):
        label = parts[i].strip()
        output = parts[i + 1].strip()
        section_outputs[label] = output

    return section_outputs


def test_part1_data_loading(captured_sections):
    """Check Part 1: first row, first five conditions, and number of patients."""
    output = captured_sections["Print the first row"]
    
    # array of expected values for the first row
    expected_first_row_values = [
        "Bobby JacksOn", "30", "Male", "B-", "Cancer", 
        "2024-01-31", "Matthew Smith", "Northview Medical", 
        "Urgent", "2024-02-02", "Paracetamol", "Normal"
    ]
    
    # array of expected medial conditions
    expected_conditions = ["Cancer", "Obesity", "Obesity", "Diabetes", "Cancer"]
    
    # expected count of pateints
    expected_count = 55500
    
    # check that each expected value is in the output
    # the output does not need to be in a specific format, just that the values appear will suffice
    for value in expected_first_row_values:
        assert value.lower() in output.lower(), (
            f"Missing expected value '{value}' from first row in output:\n{output}"
        )
    
    # check that the five conditions appear in the output
    output_lower = output.lower()
    condition_positions = []
    for condition in expected_conditions:
        pos = output_lower.find(condition.lower())
        if pos == -1:
            pytest.fail(f"Missing expected condition '{condition}' in output:\n{output}")
        condition_positions.append(pos)
    
    
    # Check for total count (55500 or 55,500)
    assert "55500" in output.replace(",", "") or "55500" in output, (
        f"Missing expected patient count in output:\n{output}"
    )


def test_part2_demographics(captured_sections):
    """Check printed age and gender distribution percentages."""
    output = captured_sections["Demographics"]
    
    # expected age distribution %
    expected_age_values = [0.21, 17.26, 29.39, 29.78, 23.37]
    
    # expected gender %
    expected_female = 49.96
    expected_male = 50.04
    
    output_lower = output.lower()
    tolerance = 0.1
    
    # extract all percentage from output
    percentage_pattern = r'(\d+\.?\d*)\s*%'
    all_percentages = re.findall(percentage_pattern, output)
    all_percentages = [float(p) for p in all_percentages]
    
    # should have at least 7 percentages (5 age groups + 2 genders)
    assert len(all_percentages) >= 7, (
        f"Expected at least 7 percentages (5 age groups + 2 genders), "
        f"but found {len(all_percentages)} in output:\n{output}"
    )
    
    # confirm that the expected age percentages are in the studetn code output
    for expected_value in expected_age_values:
        # check if any percentage in output is within the set tolerance
        found_match = False
        for found_value in all_percentages:
            if abs(expected_value - found_value) <= tolerance:
                found_match = True
                break
        
        assert found_match, (
            f"Could not find expected age percentage {expected_value}% "
            f"(within {tolerance}% tolerance) in output:\n{output}\n"
            f"Found percentages: {all_percentages}"
        )
    
    # check gender percentages specifically
    # look for "female" and "male" keywords with associated percentages
    female_match = re.search(r'female[^\d]*(\d+\.?\d*)\s*%', output_lower)
    
    if female_match:
        female_pct = float(female_match.group(1))
        assert abs(female_pct - expected_female) <= tolerance, (
            f"Female percentage mismatch. expected {expected_female}% "
            f"but found {female_pct}%"
        )
    else:
        pytest.fail(f"Could not find female percentage in output:\n{output}")
    
    # find all "male" matches but exclude those that are part of "female"
    lines = output_lower.split('\n')
    male_pct = None
    
    for line in lines:
        if 'male' in line and 'female' not in line:
            # This line contains "male" but not "female"
            match = re.search(r'(\d+\.?\d*)\s*%', line)
            if match:
                male_pct = float(match.group(1))
                break
    
    if male_pct is not None:
        assert abs(male_pct - expected_male) <= tolerance, (
            f"Male percentage mismatch: expected {expected_male}% "
            f"but found {male_pct}%"
        )
    else:
        pytest.fail(f"Could not find male percentage in output:\n{output}")


def test_part3_hospital_representation(captured_sections):
    """Check printed hospital representation percentages."""
    output = captured_sections["Hospital representation"]
    
    # Expected hospital percentages
    expected_hospitals = {
        "northview medical": 18.02,
        "riverside clinic": 12.61,
        "henderson-johnson hospital": 27.03,
        "henderson johnson hospital": 27.03,  
        "greenfield health": 32.43,
        "summit regional": 9.91,
    }
    
    output_lower = output.lower()
    tolerance = 0.1
    
    # var to find each hospital and its percentage
    hospitals_found = {}
    
    # Try to find each hospital name accounting for variations
    hospital_searches = [
        ("northview", "northview medical", 18.02),
        ("riverside", "riverside clinic", 12.61),
        ("henderson", "henderson-johnson hospital", 27.03),
        ("greenfield", "greenfield health", 32.43),
        ("summit", "summit regional", 9.91),
    ]
    
    for search_term, full_name, expected_pct in hospital_searches:
        # Look for the hospital name followed by a percentage
        pattern = rf'{search_term}[^\d]*(\d+\.?\d*)\s*%?'
        matches = re.findall(pattern, output_lower)
        
        if matches:
            found_value = float(matches[0])
            hospitals_found[full_name] = found_value
            
            # verify the value is within tolerance
            assert abs(found_value - expected_pct) <= tolerance, (
                f"Hospital percentage mismatch for {full_name}: "
                f"expected {expected_pct}% but found {found_value}%\n"
                f"Full output:\n{output}"
            )
        else:
            pytest.fail(f"Could not find hospital '{full_name}' in output:\n{output}")
    
    # verify the countof found hospitals
    assert len(hospitals_found) == 5, (
        f"Expected to find 5 hospitals, but found {len(hospitals_found)}: "
        f"{list(hospitals_found.keys())}\nFull output:\n{output}"
    )