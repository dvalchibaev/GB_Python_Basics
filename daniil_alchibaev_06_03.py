# усложненные версии до урока сделать не успеваю, постараюсь позже дополнить


# храним нужные адреса
USERS_PATH = 'users.csv'
HOBBIES_PATH = 'hobby.csv'


with open(USERS_PATH, 'r', encoding='utf-8') as f:
    users_list = [
        line.strip()
        for line in f.readlines()
    ]


with open(HOBBIES_PATH, 'r', encoding='utf-8') as f:
    hobbies_list = [
        line.strip()
        for line in f.readlines()
    ]


if __name__ == "__main__":
    if len(hobbies_list) > len(users_list):
        exit(1)

    # создаем словарь пользователей и их хобби
    users_dict = dict()
    for index in range(len(users_list)):
        # по умолчанию ставим хобби None
        # затем присваиваем если дошли до конца списка хобби
        users_dict.setdefault(users_list[index])
        if index < len(hobbies_list):
            users_dict[users_list[index]] = hobbies_list[index]

    output_file = open('users_hobby.txt', 'w', encoding='utf-8')
    for key in users_dict.keys():
        output_file.write(f"{key}: {users_dict[key]}\n")
    output_file.close()
