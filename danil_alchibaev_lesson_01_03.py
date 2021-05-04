percent_input = int(input("Введите число процентов\n"))


def percent_syntax(number):
    if number > 4:
        return "{} процентов".format(number)
    if number > 1:
        return "{} процента".format(number)
    return "{} процент".format(number)


print(percent_syntax(percent_input))
