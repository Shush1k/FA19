def input_func(goods_list, find):
    try:
        age_input = int(input("\nСколько вам лет?\nВам "))
    except ValueError:
        print("0_0 упс...")
        return
    print("\n*Товары, которые вы можете купить*")
    for goods in goods_list:
        if goods.user_age(age_input) == True:
            goods.info()
            find = True
    if not find:
        print("*Товары не найдены*")
        return