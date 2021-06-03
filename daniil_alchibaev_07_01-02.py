# Саша, привет! Не успеваю доделать задания до начала урока
# если можно, залью на GitHub что есть, потом дополню коммит до конца 02июня
# Пока код не работает, но твоя обратная связь к идее поможет:)
import os

yaml_file = 'config.yaml'


NESTING_SPACE = 4


# функция пишет файл
def write_file(file_address: str):
    open(file_address, 'w').close()


# функция создает новую папку
def create_directory(path_address: str):
    if not os.path.exists(path_address):
        os.mkdir(path_address)


# функция разбирается с текущей вложенностью
def handle_nesting(new_line: str, old_nest: int, old_path: str):
    # получаем новую вложенность напрямую из строки
    nesting_space_string = new_line.split('-')[0]
    new_nest = len(nesting_space_string) // NESTING_SPACE

    # print(old_path) самопроверка
    new_path = old_path
    # если новая вложенность не больше старой значит выходим
    # как минимум из текущей папки
    if new_nest <= old_nest:
        nest_diff = old_nest - new_nest + 1
        # убираем из адреса папки, не соответствующие новой вложенности
        # лучше работать либо только с абсолютным адресом, либо только с локальным
        # но пока не исправил
        new_path = '/'.join(old_path.split('/')[:-nest_diff])
    # костыль, если мы не создаем новую папку, то теряем символ / при обработке
    if not new_path.endswith('/'):
        new_path = new_path + '/'
    # print(new_path) самопроверка
    return new_nest, new_path


# основной парсер
def parse_yaml(yaml_file_name: str):
    stream = open(yaml_file_name, 'r', encoding='utf-8')
    current_path = os.getcwd() + '/'
    nesting = 0
    print(current_path)
    for line in stream.readlines():
        processed_line = line.strip(" -:\n\r")
        # получаем адрес дирректории для новой строки yaml
        nesting, current_path = handle_nesting(line, nesting, current_path)
        # если папка
        if line.endswith(':\n'):
            # заходим в папку, увеличиваем вложенность, создаем ее
            nesting += 1
            current_path = current_path + processed_line + '/'
            create_directory(current_path)
        else:
            # это файл, создаем его
            file_name = current_path + processed_line
            # print(file_name) проверка
            write_file(file_name)


if __name__ == "__main__":
    parse_yaml(yaml_file)
