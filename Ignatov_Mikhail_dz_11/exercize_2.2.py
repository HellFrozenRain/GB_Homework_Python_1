from exercize_2 import MyZeroDivisionError


def calc(a, b):
    try:
        if b:
            return a / b
        else:
            raise MyZeroDivisionError(calc.__name__, a, b)
    except MyZeroDivisionError as e:
        print('Ошибка:', e)


print(calc(-130, -12))
print(calc(5 * 4, 0))
