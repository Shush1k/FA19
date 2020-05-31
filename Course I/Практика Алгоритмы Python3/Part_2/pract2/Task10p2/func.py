def inp(transport_list, find):
    try:
        x1_input = int(input("Введите координату x1 -> "))
        y1_input = int(input("Ввдетие координату y1 -> "))

        x2_input = int(input("Введите координату x2 -> "))
        y2_input = int(input("Ввдетие координату y2 -> "))

        if x1_input < x2_input:
            x2_input, x1_input = x1_input, x2_input

        if y1_input < y2_input:
            y2_input, y1_input = y1_input, y2_input
    except ValueError:
        print("Упс..")
        return
    l = ([x1_input, y1_input], [x2_input, y2_input])
    print("\n*Транспорт, который вам доступен*")
    for transport in transport_list:
        if transport.Coord_func(l):
            transport.info()
            find = True
    if not find:
        print("Транспорт не найден")