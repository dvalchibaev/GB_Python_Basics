class NonNumber(Exception):
    def __init__(self, txt):
        self.text = txt


if __name__ == '__main__':
    print("import list of numbers one by one\n"
          "Enter 'stp' to finish")
    input_num_list = []
    while True:
        try:
            input_number = input()
            # we stop iterating if input is 'stp'
            if input_number == 'stp':
                break
            # check if input str in a number
            if not input_number.isnumeric():
                raise NonNumber('NaN')
            input_num_list.append(input_number)
        except NonNumber as err:
            continue
        except Exception:
            print('ooops, something else happened')
    print(input_num_list)
