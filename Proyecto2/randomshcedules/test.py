import json

# Read the JSON file
with open('generated_data/groups.json', 'r') as file:
    json_data = file.read()

# Parse the JSON data
groups = json.loads(json_data)

students = []

idCounter = 0

print(len(groups))

sum = 0

for group in groups:

    sum += int(group['capacity'])

print(sum)