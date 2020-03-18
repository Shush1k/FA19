def inputing():
    try:
        n = int(input("Введите количество транспорта: "))
    except ValueError:
        print("Некорректный ввод данных")
        return inputing()
    return n