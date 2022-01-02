"""*(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать
корректную работу с числительными, начинающимися с заглавной буквы — результат тоже
должен быть с заглавной. Например:
>>> num_translate_adv("One")
"Один"
>>> num_translate_adv("two")
"два" """


def num_translate_adv(number: str) -> str:
    if number == number.title():
        number = number.lower()
        if number in my_dict:
            return my_dict.get(number).title()

    else:
        if number in my_dict:
            return my_dict.get(number)


my_dict = {
    'zero': 'ноль',
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

a = num_translate_adv(input('enter number: '))
print(a)
