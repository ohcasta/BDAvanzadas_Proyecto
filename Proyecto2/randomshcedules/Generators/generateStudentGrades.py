import json
from selectStudent import selectStudent, generateDocument, generatePhone
import random

students = []

for number in range(1, 1484):

    student = {}
    student['id'] = number
    studentData = selectStudent()
    student['name'] = studentData[0]
    student['gender'] = studentData[1]
    student['username'] = studentData[2]
    student['document'] = generateDocument()
    student['phone'] = generatePhone()

    students.append(student)

with open('generated_data/students.json', "w") as json_file:
    # Write the JSON data to the file
    json.dump(students, json_file)

# Read the JSON file
with open('generated_data/groups.json', 'r') as file:
    json_data = file.read()

# Parse the JSON data
groups = json.loads(json_data)

studentsSubjects = []

for student in students:

    studentSubject = {}
    studentSubject['studentID'] = student['id']
    studentSubject['subjects'] = []
    studentsSubjects.append(studentSubject)

grades = []

for student in students:

    for groupSpace in range(random.randint(3, 6)):

        grade = {}
        grade['studentID'] = student['id']

        while True:
            possibleGroupId = random.randint(1, 245)
            possibleGroupName = groups[possibleGroupId-1]['subject']
            if possibleGroupName not in studentsSubjects[student['id']-1]['subjects']:
                studentsSubjects[student['id']-1]['subjects'].append(possibleGroupName)
                grade['groupID'] = possibleGroupId
                break

        grade['grade'] = round(random.uniform(1.0, 5.0), 1)

        grades.append(grade)

with open('generated_data/grades.json', "w") as json_file:
    # Write the JSON data to the file
    json.dump(grades, json_file)

    




