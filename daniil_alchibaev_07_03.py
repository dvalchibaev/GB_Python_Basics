import os
from shutil import copyfile


WORKING_DIRECTORY = 'my_project'


def move_templates(working_directory):
    for root, dirs, files in os.walk(working_directory):
        for file in files:
            if file.endswith('.html'):
                # выбираем шаблоны из файлов
                directory = os.path.join('templates', os.path.basename(root))
                # надеемся, что структура данных формата templates/dir/
                if not os.path.exists(directory):
                    os.makedirs(directory)
                from_where_to_copy = os.path.join(root, file)
                where_to_copy = os.path.join(directory, file)
                print(from_where_to_copy)
                # копируем шаблон
                copyfile(from_where_to_copy, where_to_copy)


if __name__ == "__main__":
    move_templates(WORKING_DIRECTORY)
