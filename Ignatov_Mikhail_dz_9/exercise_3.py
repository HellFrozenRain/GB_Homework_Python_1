class Worker:

    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']

class Position(Worker):

    def get_full_name(self):
        result = f'{self.name} {self.surname} {self.position}'
        return result

    def get_total_income(self):
        result = self._income_wage + self._income_bonus
        return result


peasant = Position('Пафнутий', 'Лютендорф', 'peasant', {"wage":100, "bonus": 5})
print(peasant.get_full_name())
print(peasant.get_total_income())
servant = Position('Елисей', 'Мкртчан', 'servant', {'wage':200, 'bonus': -10})
print(servant.get_full_name())
print(servant.get_total_income())