def num_translate_adv(numeral):
    if numeral[0] == numeral[0].upper():
        print(dict_1.get(numeral.lower()).capitalize())
    else:
        print(dict_1.get(numeral))

dict_1 = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

num_translate_adv(input('enter number: '))
