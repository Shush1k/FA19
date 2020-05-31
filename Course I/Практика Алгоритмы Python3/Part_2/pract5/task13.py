"""
Задача 13*:
Дан текстовый файл. Создайте двусвязный список (или массив), каждый элемент которого
содержит количество символов в соответствующей строке текста.
"""
import numpy as np

TXT_FILE = r"Priv_FA19\pract5\task13.txt"

class Node(object):

    def __init__(self, value=None, _next=None, previous=None):
        self.value = value
        self.next = _next
        self.previous = previous

    def __str__(self):
        return str(self.value)

class DLinked(object):

    def __init__(self):
        self.file2text()
        self.processing()

    def file2text(self):
        """Получаем список из строк"""
        with open(TXT_FILE, 'r') as f:
            list_m = f.readlines()
            self.text = [e.replace("\n", "") for e in list_m]

    def print_previous(self, listt):
        if listt == None:
            return
        head = listt
        tail = listt.next
        self.print_previous(tail)
        print(head, head.previous)

    def print_next(self, listt):
        if listt == None:
            return
        head = listt
        tail = listt.next
        self.print_next(tail)
        print(head, head.next)

    def processing(self):
        
        obj_arr = np.array([])
        # В данном цикле получаем кортеж из ссылок на Node obj и находим кол-во символов в строке
        for txt in self.text:
            obj_arr = np.append(obj_arr, Node(len(txt)))
            print("Длина '" + txt + "' равна " + str(len(txt)))
        # Получаем предыдущую и следующую ссылку
        for i in np.arange(obj_arr.shape[0]-1):
            obj_arr[i].next = obj_arr[i + 1]
            obj_arr[i + 1].previous = obj_arr[i]

        for i in np.arange(obj_arr.shape[0]):
            print("\n*Элемент №"+str(i)+"*")
            print("Проход с начала в конец (next)")
            self.print_next(obj_arr[i])
            print("Проход с конца в начало (previous)")
            self.print_previous(obj_arr[i])


if __name__ == "__main__":
    DLinked()