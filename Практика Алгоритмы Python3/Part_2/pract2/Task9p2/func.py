def inp(prog_list):
    try:
        print("\nПример: 20.02.2020")
        user_data = input("Введите дату:")

    except ValueError:
        print("0_0 упс...")
        return

    find = False
    print("\n*ПО, которое вам доступно*")
    for prog in prog_list:
        if prog.date_PO(user_data) == True:
            prog.info()
            find = True
    if not find:
        print("*Товары не найдены*")
        return