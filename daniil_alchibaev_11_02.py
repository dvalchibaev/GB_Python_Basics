class DivByZero(Exception):
    def __ini__(self, text):
        self.text = text


if __name__ == "__main__":
    import sys
    try:
        _, input_1, input_2 = sys.argv
        if int(input_2) == 0:
            raise DivByZero("Деление на ноль!")
    except DivByZero as err:
        print(err)
    except Exception:
        print("Что-то другое")
    else:
        output = int(input_1) / int(input_2)
        print(output)
