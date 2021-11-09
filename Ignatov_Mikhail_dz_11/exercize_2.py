class MyZeroDivisionError(BaseException):
    def __init__(self, function, a, b):
        msg = f'деление на нуль в {function}\n {a = }, {b = }'
        super().__init__(msg)