import pandas as pd
import random
from randomTeacher import selectTeacher
from dayOfWeek import selectStartDay, selectFinalDay, selectHours, selectClassrooms
from Faculty import selectFaculty
from replace_accents import replace_accents
import json

docentes = pd.read_csv('data/Docentes.csv')
asignaturas = pd.read_csv('data/Asignaturas.csv')

groups = []
idCounter = 1

for index, row in asignaturas.iterrows():

    for number in range(random.randint(2, 4)):

        group = {}
        group['id'] = idCounter
        group['number'] = number+1
        group['subject'] = replace_accents(row['Asignatura'])
        group['teacher'] = replace_accents(selectTeacher(row['Tipo']))
        group['faculty'] = selectFaculty(row['Tipo'])
        group['start'] = '26-08-2023'
        group['end'] = '05-12-2023'
        group['duration'] = 'Semestral'
        group['journey'] = 'Diurno'
        group['capacity'] = random.randint(25, 35)

        groups.append(group)
        idCounter += 1

with open('generated_data/groups.json', "w") as json_file:
    # Write the JSON data to the file
    json.dump(groups, json_file)

schedules = []
days = ['Lunes', 'Martes', 'Miercoles']

for group in groups:

    startingDay = selectStartDay()
    finalDay = selectFinalDay(startingDay)
    hours = selectHours()
    firstClassroom = selectClassrooms()

    if random.randint(1, 6) == 1:
        lastClassroom = selectClassrooms()
    else:
        lastClassroom = firstClassroom

    FirstSchedule = {}
    FirstSchedule['groupID'] = group['id']
    FirstSchedule['weekday'] = startingDay
    FirstSchedule['start'] = hours[0]
    FirstSchedule['end'] = hours[1]
    FirstSchedule['classroom'] = firstClassroom

    LastSchedule = {}
    LastSchedule['groupID'] = group['id']
    LastSchedule['weekday'] = finalDay
    LastSchedule['start'] = hours[0]
    LastSchedule['end'] = hours[1]
    LastSchedule['classroom'] = lastClassroom

    schedules.append(FirstSchedule)
    schedules.append(LastSchedule)

with open('generated_data/schedules.json', "w") as json_file:
    # Write the JSON data to the file
    json.dump(schedules, json_file)