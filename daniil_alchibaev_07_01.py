# Саша, привет! Не успеваю доделать задания до начала урока
# если можно, залью на GitHub что есть, потом дополню коммит до конца 02июня
# Пока код не работает, но твоя обратная связь к идее поможет:)
import os

yaml_file = 'config.yaml'


NESTING_SPACE = 4


# функция пишет файл
def write_file(file_address):
    open(file_address, 'w').close()


# функция создает новую папку
def create_directory(path_address):
    if not os.path.exists(path_address):
        os.mkdir(path_address)


# функция разбирается с текущей вложенностью
def handle_nesting(nest, dir_path, new_line):
    new_nest = new_line.split('-')[0] // NESTING_SPACE
    if nest < new_nest:
        updated_path = dir_path + '/' + new_line
    elif nest > new_nest:
        updated_path = ''.join(dir_path.split('/')) + '/' + new_line
    else:
        updated_path = dir_path
    return new_nest, updated_path


# основной парсер
def parse_yaml(yaml_file_name):
    stream = open(yaml_file_name, 'r', encoding='utf-8')
    current_path = os.getcwd()
    nesting = 0
    print(current_path)
    for line in stream.readlines():
        processed_line = line.strip('- :\n\r')
        print(processed_line)
        if line.endswith(':\n'):
            create_directory(processed_line)
        else:
            write_file(current_path + '/' + processed_line)


if __name__ == "__main__":
    parse_yaml(yaml_file)
