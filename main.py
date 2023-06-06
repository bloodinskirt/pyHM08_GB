import function

while True:
    print('1. вывод, 2. добавление, 3. поиск')
    mode = int(input())
    if mode == 1:
        function.show_data()
    elif mode == 2:
        function.add_data()
    elif mode == 3:
        function.find_data()
    else:
        break