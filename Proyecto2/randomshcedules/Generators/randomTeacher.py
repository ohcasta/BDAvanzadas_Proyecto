import random
import pandas as pd

def selectTeacher(classType):

    if classType == 'FUND. OPTATIVA (O)' or classType == 'FUND. OBLIGATORIA (B)':
        indexToSelect = random.randint(40, 58)
    else:
        indexToSelect = random.randint(0, 39)

    teachers = pd.read_csv('data/Docentes.csv')
    return teachers.loc[indexToSelect]['Docente']