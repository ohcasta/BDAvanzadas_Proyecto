import random
import pandas as pd
from replace_accents import replace_accents

def selectStudent():

    genders = ['Hombre', 'Mujer']
    selectedGender = random.choice(genders)

    if selectedGender == 'Hombre':
        name_path = 'data/hombres.csv'
        nameIndex = random.randint(0, 25441)
    else:
        name_path = 'data/mujeres.csv'
        nameIndex = random.randint(0, 24493)

    names = pd.read_csv(name_path)
    selectedName = replace_accents(names.loc[nameIndex]['nombre'])

    lastNameIndex = random.randint(0, 25848)
    lastNames = pd.read_csv('data/apellidos.csv')

    selectedLastName = replace_accents(lastNames.loc[lastNameIndex]['apellido'])

    fullName = selectedName + ' ' + selectedLastName
    username = selectedName[0].lower() + selectedLastName.replace(' ', '').lower()

    return [fullName, selectedGender, username]

def generateDocument():
    min_value = 10**6  # Minimum value with 7 digits (inclusive)
    max_value = (10**7) - 1  # Maximum value with 7 digits (inclusive)
    return '100' + str(random.randint(min_value, max_value))

def generatePhone():
    min_value = 10**7  # Minimum value with 8 digits (inclusive)
    max_value = (10**8) - 1  # Maximum value with 8 digits (inclusive)
    return '30' + str(random.randint(min_value, max_value))
