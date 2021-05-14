def num_translate_adv(input_number):
    eng_numbers = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten")
    rus_numbers = ("ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять")
    if not input_number or str(input_number).lower() not in eng_numbers:
        return None
    eng_to_rus_numbers = {eng_numbers[i]: rus_numbers[i] for i in range(len(eng_numbers))}
    if input_number[0].isupper():
        return (eng_to_rus_numbers[input_number.lower()]).capitalize()
    return eng_to_rus_numbers[input_number]


print(num_translate_adv(""))
print(num_translate_adv(1))
print(num_translate_adv("123"))
print(num_translate_adv("zero"))
print(num_translate_adv("Six"))
