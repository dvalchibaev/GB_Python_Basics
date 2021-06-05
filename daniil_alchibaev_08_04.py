def val_checker(callback):
    def _val_checker(func):
        def wrapper(*argv):
            if callback(*argv):
                result = func(*argv)
                return result
            else:
                raise ValueError(f'Wrong input: {argv}')
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(num):
    return num ** 3


print(calc_cube(3))
print(calc_cube(-3))
