def inp(client_list, find):
    try:
        print("\nПример: 20.02.2020")
        user_date = input("Введите дату, чтобы найти клиента: ")
    except ValueError:
        print("0_0 упс...")
        return
    print("\n*Клиенты, которые начали сотрудничать с банком в заданную дату*")
    for client in client_list:
        if client.client_date(user_date) == True:
            client.info()
            find = True
    if not find:
        print("*Клиенты не найдены*")
        return