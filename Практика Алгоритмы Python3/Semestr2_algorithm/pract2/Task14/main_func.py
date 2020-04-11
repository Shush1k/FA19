import classCurency, classDollar, classEuro
def main():
    try:
        choice = input("1)Купить\n2)Продать\nВыбор:")
        if choice != "1" and choice != "2":
            raise KeyError
        curr_choice = int(input("1)Евро\n2)Доллары\nВыбор:"))
        if curr_choice != 1 and curr_choice != 2:
            raise KeyError
        pers_money = float(input("Ваше количество денег:"))
    except ValueError:
        print("Некорректный ввод данных")
    except KeyError:
        print("Некорректный ввод данных")
        return
    d = {
        1: classEuro.Euro,
        2: classDollar.Dollar
    }
    currency_list = [d[curr_choice](pers_money, choice) for _ in range(1)]
    for curr in currency_list:
        curr.info(choice)