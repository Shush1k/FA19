# from random import randint
# # Создание списка
# test1 = []
# for i in range(5):
#     test1.append(randint(1, 10))
# # через генератор
# test2 = [randint(1,10) for i in range(5)]
# print("Список 1:", test1)
# print("Список 2:", test2)

# print("\nКол-во различных чисел:")
# print("В списке 1: ", len(set(test1)))
# print("В списке 2: ", len(set(test2)))


# print("\nОбщие числа двух списков")
# extended_list = []
# extended_list.extend(test1)
# extended_list.extend(test2)
# extended_list = list(set(extended_list))
# print(extended_list)

# # Удаление из списка 1 чисел из списка 2
# print("\nУдаление из списка 1 чисел из списка 2")
# test1 = list(set(test1) - set(test2))

# print(test1)

# # Второй способ
# test_1_set = set(test1)
# test_2_set = set(test2)
# test_1_set.difference_update(test_2_set)
# print(list(test_1_set))

#Задача 2
# stud_list = [["Петров", 3, 4, 5], ["Иванов", 1, 4, 4], ["Королёв", 2, 5, 4]]

# print("\nСредний балл:")
# avg_hist = 0
# avg_math = 0
# avg_inf = 0
# for student in range(len(stud_list)):
#     for i, value in enumerate(stud_list[student]):
#         if i == 1:
#             avg_hist += value
#         elif i == 2:
#             avg_math += value
#         elif i == 3:
#             avg_inf += value

# print("СР История: ",avg_hist/len(stud_list))
# print("СР Алгебра: ",avg_math/len(stud_list))
# print("СР Информатика: ",avg_inf/len(stud_list))
