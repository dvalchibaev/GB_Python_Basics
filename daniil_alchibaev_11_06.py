# Пока что, дублировал задание 4
class Warehouse:
    def __init__(self, name):
        self.name = name


class Equipment:
    def __init__(self, eq_name):
        self.eq_name = eq_name


class Printer(Equipment):
    def __init__(self, eq_name, ink_max, ink=0):
        self.ink = ink
        self.ink_max = ink_max
        super().__init__(eq_name)

    def is_empty(self):
        return self.ink == 0

    def is_full(self):
        return self.ink == self.ink_max


class Scanner(Equipment):
    def scan_file(self, input_file):
        print(f"{self.eq_name} scans file: {input_file}")


class Xerox(Equipment):

    def xerox_print(self, file):
        print(f'{file} is printed by {self.eq_name}')
        return file
