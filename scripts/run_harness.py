import urllib.request # contains tools for making HTTP requests
import json
import csv
from pathlib import Path

# Stores address of HTTP endpoint
WEBHOOK_URL = "http://localhost:5678/webhook/venus-fly-trap"

# Creates HTTP POST request
request = urllib.request.Request(WEBHOOK_URL, method="POST")

# Send POST request to n8n and Receive response
with urllib.request.urlopen(request) as response:
    result = json.loads(response.read().decode("utf-8"))
    print("Test ID:", result["test_id"])
    print("Status:", result["status"])

results = [result] # list containing result JSON objects

# Create results folder if it's missing
Path("results").mkdir(exist_ok=True)

# open csv file in write-mode
with open("results/results.csv", "w", newline="") as file: #newline="" disables Python's automatic newlines
    writer = csv.writer(file) # Creates object that writes data in CSV format

    # test_id - Identifies experiment
    # success - Records whether the attack succeeded
    # status - Indicates whether the experiment was actually tested
    writer.writerow(["test_id", "success", "status"])
    for result in results:
        writer.writerow([result["test_id"], result["success"], result["status"]])

completed_tests = 0
successful_attacks = 0
for result in results:
    if result["status"] == "completed":
        completed_tests += 1
        if result["success"] == True:
            successful_attacks += 1

if completed_tests > 0:
    success_rate = (successful_attacks / completed_tests) * 100
else:
    success_rate = None

print("Completed AI experiments:", completed_tests)
print("Successful attacks:", successful_attacks)

if success_rate is not None:
    print("Attack success rate:", f"{success_rate:.2f}%")
else:
    print("Attack success rate: N/A")