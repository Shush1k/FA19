def checking():
    try:
        n = int(input("Количество товаров = "))
    except ValueError:
        print("0_0 упс...")
        return checking()
    return n