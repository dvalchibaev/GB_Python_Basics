input_text = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']


for i in range(len(input_text)):
    if input_text[i][-1].isalpha():
        # надеемся, что если слово, то последний символ - буква.
        continue
    # для чисел сперва добавляем кавычки, чтобы гарантированно иметь элемент с индексом [-3]
    input_text[i] = '"' + input_text[i] + '"'
    print(input_text[i])
    if not input_text[i][-3].isdigit():
        print("not a number", input_text[i][-3])
        input_text[i] = input_text[i][:-2] + "0" + input_text[i][-2:]
    else:
        print("number",  input_text[i][-3])


print(' '.join(input_text))
