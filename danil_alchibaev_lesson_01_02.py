odd_cubic = [i ** 3 for i in range(1, 1000, 2)]


def sum_sevens(numbers, shift=0):
    output_sum = 0
    for i in numbers:
        value = i + shift
        inner_sum = 0
        while value:
            inner_sum += value % 10
            value = value // 10
        if inner_sum % 7 == 0:
            output_sum += i
    return output_sum


print(sum_sevens(odd_cubic))
print(sum_sevens(odd_cubic, 17))
