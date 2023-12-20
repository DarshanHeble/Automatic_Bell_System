import re

data_list = [
    {"time": "07:56 PM", "text": "period(1)", "days": ["Wed"], "switch_state": True},
    {"time": "07:56 PM", "text": "period(2)", "days": ["Wed"], "switch_state": True},
    {"time": "07:56 PM", "text": "period(4)", "days": ["Wed"], "switch_state": True},
    {
        "time": "07:56 PM",
        "text": "other_period(3)",
        "days": ["Wed"],
        "switch_state": True,
    },
]

# Extracting numerical part from the "text" values using re for the "period()" format
extracted_numbers = [
    int(match.group(1))
    for item in data_list
    if (match := re.match(r"period\((\d+)\)", item["text"]))
]

# Find missing values in the sequence
n = max(extracted_numbers)
missing_values = [str(i) for i in range(1, n + 1) if i not in extracted_numbers]

# Displaying the result
if missing_values:
    print(f"Missing values: {', '.join(missing_values)}")
else:
    print(n + 1)
