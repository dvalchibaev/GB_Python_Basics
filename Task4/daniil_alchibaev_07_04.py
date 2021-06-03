import os
import json


# reading files in a given folder
FOLDER_NAME = 'some_data'
files_in_folder = os.listdir(FOLDER_NAME)
# get file sizes and types as lists
file_sizes = [
    os.stat(f'{FOLDER_NAME}/{file}').st_size
    for file in files_in_folder
]
file_types = [file.split('.')[-1] for file in files_in_folder]


# get max size of file
max_file_size = sorted(file_sizes, reverse=True)[0]
max_decimal_digits = len(str(max_file_size)) + 1


# make stats dict in format {100: [n, {'xxx', 'yyy', ...}], ...}
files_stats = dict()
COUNT_INDEX = 0
TYPES_INDEX = 1
for index in range(len(files_in_folder)):
    size = file_sizes[index]
    file_type = file_types[index]

    # go from 100 to 10 ** max_decimal_digits until
    # file size is lower
    for digits_number in range(2, max_decimal_digits):
        power_of_ten = 10 ** digits_number

        files_stats.setdefault(
            # вот тут я не понял, почему пайчарм это выделяет
            # элементы кортажа же поменять не даст
            power_of_ten, [0, set()]
        )

        if size < power_of_ten:
            # adding data to files_stats dict
            files_stats[power_of_ten][COUNT_INDEX] += 1
            files_stats[power_of_ten][TYPES_INDEX].add(file_type)
            break


# convert output dict to format {100: (n, ['xxx', 'yyy', ...]), ...}
for key in files_stats.keys():
    (files_stats[key])[TYPES_INDEX] = list(files_stats[key][TYPES_INDEX])
    files_stats[key] = tuple(files_stats[key])
print(files_stats)

# dump output dict to json file
with open(f'{FOLDER_NAME}/output.json', 'w') as jf:
    json.dump(files_stats, jf)
