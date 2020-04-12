import classGoods
def input_func(all_obj, find):
    try:
        user_money = float(input("Кол-во денег пользователя = "))
    except ValueError:
        print("0_0 упс...")
        return
    print("Вам хватает денег на эти товары:")
    for obj in all_obj:
        if obj.SUBJ(user_money) == True:
            obj.info()
            find = True
    if find == False:
        print("*Товары не найдены*")
        return