# доделаю после урока

def val_checker(fun):
    def wrapper(*argv):
        return fun(*argv)
    return wrapper


@val_checker
def calc_cube(num):
    return num ** 3


print(calc_cube(3))
