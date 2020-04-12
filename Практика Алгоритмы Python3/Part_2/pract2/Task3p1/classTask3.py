import classmethods
class Task3:
    def __init__(self):
        print("Task3")
        try:
            d = {"1": self.user_input, "2": self.random_input}
            self.my_list = []
            self.my_list_len = int(input("Длина последовательности = "))
            choice = input("Как заполнить последовательность?\n1. Вручную\n2. Рандомно\nВыбор: ")
            
            if choice in d:
                d[choice]()
                self.out_list()
            else:
                print("Некорректный ввод")
        except Exception as e:
            print("¯\\_(ツ)_/¯ Ошибка: ", e)
    classmethods.check
    user_input = classmethods.user_input
    random_input = classmethods.random_input
    out_list = classmethods.out_list