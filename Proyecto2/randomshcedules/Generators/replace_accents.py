def replace_accents(input_string):
    accents = {
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u',
        'Á': 'A',
        'É': 'E',
        'Í': 'I',
        'Ó': 'O',
        'Ú': 'U',
        'ñ': 'n',
        'Ñ': 'N'
    }

    output_string = ""
    for char in input_string:
        if char in accents:
            output_string += accents[char]
        else:
            output_string += char

    return output_string
