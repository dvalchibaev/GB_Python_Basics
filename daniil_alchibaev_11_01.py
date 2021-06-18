class DateLesson:
    def __ini__(self, date_string: str):
        self.day, self.month, self.year = map(int, date_string.split('-'))

    @classmethod
    def str_to_date(cls, date_string: str):
        return map(int, date_string.split('-'))

    @staticmethod
    def is_year_leap(year: int) -> bool:
        return year % 4 == 0

    @staticmethod
    def check_date(day: int, month: int, year: int):
        valid_month = [number for number in range(1, 13)]
        # первая проверка, что месяц в нужном диапазоне и день хотя бы положительный
        if month not in valid_month or day <= 0:
            return False
        # если февраль
        if month == 2:
            if DateLesson.is_year_leap(year):
                # год високосный
                return day <= 29
            else:
                # год не високосный
                return day <= 28
        # проверяем корректность даты для остальных месяцев
        if month in {1, 3, 5, 7, 8, 10, 12}:
            return day <= 31
        else:
            return day <= 30


if __name__ == '__main__':
    day1, month1, year1 = DateLesson.str_to_date('17-06-2021')
    day2, month2, year2 = DateLesson.str_to_date('30-02-2018')
    print(day1, month1, year1, DateLesson.check_date(day1, month1, year1))
    print(day2, month2, year2, DateLesson.check_date(day2, month2, year2))
