# предварительная версия, разбираюсь с правильной версией try-except
# любопытно, что не было заданий на исключения в уроке 7
import re


def email_parse(email_line):
    # регулярное выражение типа слово + @ + слово + . + 2-3 англ символа
    RE_EMAIL = re.compile(r"^\w+@\w+\.[a-z]{2,3}")
    try:
        # основная проверка, что мы получили RE_EMAIL не None
        email = RE_EMAIL.fullmatch(email_line).string
        username, domain = email.split('@')
        return {'username': username,
                'domain': domain}
    except Exception as exc:
        raise AttributeError(f'wrong email: {email_line}') from exc


print(email_parse('abs@abs.ru'))
print(email_parse('employee@company.com'))
print(email_parse('error@here'))
