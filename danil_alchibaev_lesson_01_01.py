duration = int(input("Enter a time duration in sec\n"))
input_time = duration


def add_answer(output_text, number, text):
    return '{} '.format(number) + text + ', ' + output_text


# с детализацией на месяц есть неоднозначность, пропустил этот шаг
# по хорошему, с годами тоже, но тут уже надо какой-нибудь date-time подключать
minutes = 60
hours = minutes * 60
days = hours * 24
years = days * 365


seconds = duration % 60
answer_text = '{} sec'.format(seconds)


input_time, input_years = (input_time % years, input_time // years)
input_time, input_days = (input_time % days, input_time // days)
input_time, input_hours = (input_time % hours, input_time // hours)
input_time, input_minutes = (input_time % minutes, input_time // minutes)


# есть подозрение, что и тут можно все свести к простой функции
if input_minutes:
    answer_text = add_answer(answer_text, input_minutes, "min")
if input_hours:
    answer_text = add_answer(answer_text, input_hours, "hrs")
if input_days:
    answer_text = add_answer(answer_text, input_days, "days")
if input_years:
    answer_text = add_answer(answer_text, input_years, "years")


print(answer_text)
