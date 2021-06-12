class Worker:
    def __init__(self, first_name, last_name, position, wage, bonus):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_total_income(self):
        return f'{self._income["wage"] + self._income["bonus"]}'


if __name__ == '__main__':
    ceo_position = Position('Jeff', 'Bezos', 'CEO', 1e7, 6.5e7)
    print(ceo_position.get_total_income())
