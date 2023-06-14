import random

def selectStartDay():
    startingDaysOptions = ['Lunes', 'Martes', 'Miercoles']
    return random.choice(startingDaysOptions)

def selectFinalDay(startingDay):
    finalDaysOptions = {
        'Lunes' : 'Miercoles',
        'Martes' : 'Jueves',
        'Miercoles' : 'Viernes'
    }

    return finalDaysOptions[startingDay]

def selectHours():
    hours = [7, 9, 11, 2, 4, 6]
    startingHour = random.choice(hours)
    finalHour = (startingHour + 2) % 12

    return (str(startingHour) + ':00', str(finalHour) + ':00')

def selectClassrooms():

    buildings = [401, 453, 454]
    floor = [100, 200, 300]
    room = random.randint(1, 10)

    return [random.choice(buildings), random.choice(floor) + room]