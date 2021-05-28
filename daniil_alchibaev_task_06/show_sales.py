# усложненные версии до урока сделать не успеваю, постараюсь позже дополнить


# надеемся, что вводился корректный формат данных вида "XXXX,X\n"
SYMBOLS_IN_LINE = 7


if __name__ == "__main__":
    import sys
    sales = open("bakery.csv", 'r', encoding='utf-8')
    # определяем начальную и конечную ЛИНИЮ выгрузки по умолчанию
    start_line = 1
    end_line = 1 + sales.seek(0, 2) // SYMBOLS_IN_LINE

    # обрабатываем ввод с консоли
    if len(sys.argv) == 2:
        _module_name, start_line = sys.argv

    if len(sys.argv) == 3:
        _module_name, start_line, end_line = sys.argv

    # определяем начальную и конечную символьную позицию
    start_position = (int(start_line) - 1) * SYMBOLS_IN_LINE
    end_position = (int(end_line) - 1) * SYMBOLS_IN_LINE
    # пока начальная позиция не больше конечной - печатаем построчно
    while start_position <= end_position:
        # print(f"start = {start_position}, end = {end_position}") отладка
        sales.seek(start_position)
        line = sales.readline()
        print(line)
        # после печати линии, сдвигаем курсор на следущую строку
        start_position = start_position + SYMBOLS_IN_LINE
