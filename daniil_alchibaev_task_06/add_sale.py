if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        _module_name, input_sales = sys.argv
        # открываем файл с добавлением данных в конец
        sales_file = open("bakery.csv", 'a', encoding='utf-8')
        # добавляем данные
        sales_file.write(f"{input_sales}\n")
        sales_file.close()
