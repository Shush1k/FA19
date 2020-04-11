from random import randint
def check(self, abc):
    try:
        return int(abc)
    except ValueError:
        return abc
        
def user_input(self):
    """
    Ввод с клавиатуры
    """
    for i in range(self.my_list_len):

        res = self.check(input("Введите №"+str(i+1)+" элемент: "))
        self.my_list.append(res)

def random_input(self):
    self.my_list = [randint(-10, 10) for _ in range(self.my_list_len)]

def out_list(self):
    print("Последовательность:")
    print(self.my_list)