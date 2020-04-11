def checking():
    try:
        n = int(input("Введите количество транспорта: "))
    except ValueError:
        print("Некорректный ввод данных")
        return checking()
    return n