class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'полное имя работника {self.name} {self.surname}')

    def get_total_income(self):
        total_income = sum(self._income.values())
        print(f'зарплата работника {total_income}')


person = Position('Adam', 'Smith', 'Lawyer', 50, 100)
person.get_full_name()
print(f"должность работника {person.position}")
person.get_total_income()
