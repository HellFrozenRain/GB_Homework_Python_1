import datetime

class Date:
    def __init__(self, dd_mm_year):
        self.dd_mm_year = str(dd_mm_year)

    @classmethod
    def str_date_to_integer(cls, dd_mm_year):
        day, month, year = dd_mm_year.split('-')
        cls.date_as_int = tuple(map(int, [year, month, day]))
        return cls.date_as_int

    @staticmethod
    def date_validation(int_date):
        is_valid_date = True
        try:
            datetime.datetime(*int_date)
        except ValueError:
            is_valid_date = False

        if is_valid_date:
            print("Input date is valid.")
        else:
            print("Input date is not valid.")


result = Date.str_date_to_integer('28-02-2021')
print(*result, sep='-')
Date.date_validation(result)
result = Date.str_date_to_integer('30-02-2190')
print(*result, sep='-')
Date.date_validation(result)