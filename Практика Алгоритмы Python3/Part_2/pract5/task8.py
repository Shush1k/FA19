"""
Задача 8:
Пользователь вводит упорядоченный список/массив книг (заданной длины по алфавиту).
Добавить новую книгу, сохранив упорядоченность списка по алфавиту
"""
import numpy as np
alp = np.array([])
book_list = input("Список книг: ").split()
alp = np.append(alp, book_list)
alp = np.sort(alp)
b = input("Добавить книгу: ")         
alp = np.append(alp, b)       
alp = np.sort(alp)
print(alp)