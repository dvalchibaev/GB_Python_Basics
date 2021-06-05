def type_logger(fun):
    def wrapper(*argv):
        # получаем результат выполнения функции
        result = fun(*argv)
        # собираем типы аргументов
        arg_types = ''
        for arg in argv:
            str_type = str(type(arg))
            arg_types = arg_types + ', ' + str_type
        return f'{result}:{arg_types}'
    return wrapper


# первая функция для проверки
@type_logger
def cubes(number):
    return number ** 3


# вторая функция для проверки
@type_logger
def check_with_multiple(num: int, string: str):
    return num, string


print(cubes(3, 2))
print(check_with_multiple(2, 'ok'))
