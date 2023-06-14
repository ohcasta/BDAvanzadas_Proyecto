def selectFaculty(classType):

    if classType == 'FUND. OPTATIVA (O)' or classType == 'FUND. OBLIGATORIA (B)':
        return 'Facultad de Ciencias'
    else:
        return 'Facultad de Ingenieria'