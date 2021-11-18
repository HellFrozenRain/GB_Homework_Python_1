class OnlyNumbersError(Exception):
    def __init__(self):
        msg = f'OnlyNumbersError: expected number not string'
        super(OnlyNumbersError, self).__init__(msg)


def to_number(num):
    if num.isdigit():
        return int(num)
    else:
        try:
            return float(num)
        except ValueError:
            try:
                if num != 'stop':
                    raise OnlyNumbersError()
            except OnlyNumbersError as e:
                print(e)


number_list = []
input_data = ''
while input_data != 'stop':
    input_data = input('Enter a number: ')
    number = to_number(input_data)
    if number:
        number_list.append(number)
print(f'Formed list with numbers: {number_list}')