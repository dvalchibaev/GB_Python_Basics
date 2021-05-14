def thesaurus_adv(*args):
    """
    :param args: names formated "FirstName LastName"
    :return: dict of names, sorted by 1st letter of LastName then FirstName
    """
    thesaurus_dict = dict()
    for name in args:
        first_name, last_name = name.split(" ")
        if not thesaurus_dict.get(last_name[0]):
            # если на данную букву фамилии словарь еще не заводился, то создаем новый
            thesaurus_dict[last_name[0]] = {first_name[0]: name}
        elif thesaurus_dict[last_name[0]].get(first_name[0]):
            # увидел ошибку во время вебинара, исправил кривовато, но чтобы было минимум красного
            thesaurus_dict[last_name[0]][first_name[0]].append(name)
        else:
            thesaurus_dict[last_name[0]].setdefault(first_name[0], [])
    return thesaurus_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
