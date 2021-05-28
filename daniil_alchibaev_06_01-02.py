with open("nginx_logs.txt", 'r') as file:
    IP_INDEX = 0
    COMMAND_INDEX = 5
    PATH_INDEX = 6
    open('output.txt', 'w').close()
    # надеемся, что памяти хватит хотя бы на словарь
    hackers_actions_dict = dict()
    for line in file:
        line_blocks = line.split()
        # считываем ip, запрос и путь в строке
        user_ip = line_blocks[IP_INDEX]
        user_command = line_blocks[COMMAND_INDEX]
        user_path = line_blocks[PATH_INDEX]
        # обновляем кол-во действий пользователя с данным ip
        hackers_actions_dict.setdefault(user_ip, 0)
        hackers_actions_dict[user_ip] += 1
        # добавляем новую строку в файл output.txt в формате
        # (<remote_addr>, <request_type>, <requested_resource>)
        output_line = open("output.txt", 'a')
        output_line.write(
            f'({user_ip}, {user_command}, {user_path})\n'
        )
        output_line.close()

# проверяем задачу 1
with open("output.txt", 'r') as file:
    for _ in range(2):
        print(file.readline())

# решение задачи 2
max_actions = 0
hacker = None
for key in hackers_actions_dict.keys():
    if hackers_actions_dict[key] > max_actions:
        hacker = key
        max_actions = hackers_actions_dict[key]
print(f"User ip is {hacker}, # of requests {hackers_actions_dict.get(hacker)}")
