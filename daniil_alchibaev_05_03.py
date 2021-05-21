# назвал как в ТЗ
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Александр', 'Даниил'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def tutors_pairs_generator(tutor: list, klass: list):
    for index in range(len(tutor)):
        if index < len(klass):
            yield tutors[index], klass[index]
        else:
            yield tutor[index], None


# проверка генератора со случаями (<tutor>, None) и ошибкой StopIteration
tutor_klasses_pairs = tutors_pairs_generator(tutors, klasses)
for _ in range(len(tutors)+1):
    print(next(tutor_klasses_pairs))
