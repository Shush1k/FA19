def inp(toy_list):
    try:
        user_color = str(input("\nВведите цвет!\nВаш цвет: "))

    except ValueError:
        print("0_0 упс...")
        return

    find = False
    print("\n*Игрушки с заданным цветом*")
    for toy in toy_list:
        if toy.toy_color(user_color) == True:
            toy.info()
            find = True

    if not find:
        print("*Товары не найдены*")