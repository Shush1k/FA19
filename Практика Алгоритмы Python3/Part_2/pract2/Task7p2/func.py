def inp(persons_list, find):
    try:
        input_name = input("Введите фамилию, чтобы найти персону: ")
    except ValueError:
        print("Упс....")
        return
    print("\n*Персоны:*")
    for pers in persons_list:
        if pers.pers_search(input_name):
            find = True
            pers.info()
    if not find:
        print("*Персоны не найдены*")
        return