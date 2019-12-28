#!/usr/bin/env python
# coding: utf-8

# In[4]:


#GAME
from random import randint
"""Описание игры:

На шахматной доске в некоторых клетках случайно разбросаны
фишки.Игроки ходят по очереди.За один ход можно снять все фишки с какой-либо 
горизонтали или вертикали, на которой они есть. Выигрывает тот,
кто заберет последние фишки.

"""


def xboard():
    
    print("   A B C D E F G H")
    for i in range(0, 8):
        symb = ""
        for j in range(0, 8):
            if board[i][j] == 1:      
                symb += " ◙"   
            else:
                symb += " ○"
        
        print(i, symb)
# Создаем поле,заполняя символами ◙ и ○.
        
def players():
    
    if n%2 != 0:
        return 'Игрок 1'       
    else:
        return 'Игрок 2'

    
def count_buttons():
    
    k=0
    for i in range(0, 8):
        for j in range(0, 8):  # Кол-во пуговиц на поле
            k += board[i][j]
    return k


while True:
    input_start = input("Введите start для запуска,end для завершения программы:")
    if input_start == "start":
        print("""Описание игры:

На шахматной доске в некоторых клетках случайно разбросаны фишки.
Игроки ходят по очереди.За один ход можно снять все фишки с какой-либо 
горизонтали или вертикали, на которой они есть. Выигрывает тот,кто заберет 
последние фишки.

        """)
        n=1
        board = [
                [randint(0,1) for x in range(8)],
                [randint(0,1) for x in range(8)],
                [randint(0,1) for x in range(8)],
                [randint(0,1) for x in range(8)],
                [randint(0,1) for x in range(8)],
                [randint(0,1) for x in range(8)],
                [randint(0,1) for x in range(8)],
                [randint(0,1) for x in range(8)]
                ]
        xboard()
        k = count_buttons()

        while k > 0:                          # Игра идет пока кол-во фишек >0
            c=0
            x = (input("Введите букву или цифру:"))
            if not (len(x) == 1):
                print("Введите положительную цифру от 0 до 7 или букву латинского алфавита от A до H")
                continue
            if x.isnumeric() == True:     
                x = int(x)
                if 0 <= x < 8:
                    for i in range(0, 8):    # Проверка на наличие пуговиц для строки.
                        if board[x][i] == 0:  
                            c += 1
                    if c == 8:
                        print("Это строка не содержит пуговиц")
                        continue
                    for i in range(0, 8):   # Заполняем строку нулями.
                        board[x][i] = 0
                else:
                    print("Введите число 0—7")
                    continue
            else:                      # Если не цифра,то выполняется этот код.
                x = x.upper()
                x = ord(x) - ord("A")   
                if 0 <= x < 8:
                    for i in range(0, 8):
                        if board[i][x] == 0:
                            c += 1           # Проверка на наличие пуговиц для столбца.
                    if c == 8:
                        print("Этот столбец не содержит пуговиц")
                        continue
                    for i in range(0, 8):   # Заполняем столбец нулями.
                        board[i][x] = 0
                else:
                    print("Введите букву A—H")
                    continue

            player = players()
            print('Ход игры —', n)
            print("Ходит", player)            
            xboard()    # Выводим поле
            k = count_buttons()   # Изменяем кол-во фишек
            n += 1        # Ход игры
        print(player,"победил :3","игра длилась",n-1,"ходов")
    elif input_start == "end":
        print("-----------------------------------------------------------------------------".center(75))
        print("Вы решили завершить программу".center(75))
        print("-----------------------------------------------------------------------------".center(75))
        break
    else:
        print("Неверный ввод")
input()


# In[31]:


print("Вы решили завершить игру".center(75))
print("-------------------------------------------------------------------------------".center(75))


# In[ ]:




