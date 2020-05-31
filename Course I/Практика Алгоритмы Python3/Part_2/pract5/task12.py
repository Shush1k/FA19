"""
Задача 12:
Пусть элементы списка/массива хранят символы предложения. Замените каждое вхождение слова
"itmathrepetitor" на "silence".
"""
import array as ar

def func(curr_list):
    res = curr_list[:]
    len_m = len('itmathrepetitor')
    len_s = len('itmathrepetitor') - len('silence')
    for i in range(len(curr_list)):
        if ''.join(curr_list[i:i+len_m]) == 'itmathrepetitor':
            res[i:i+len_m] = ar.array('u', 'silence00000000')

    for i in range(len(curr_list)):
        if ''.join(res[i:i+len_s]) == '00000000':
            for _ in range(len_s):
                res.pop(i)
    return res


if __name__ == '__main__':
    my_str = "\nЛа ла ля какой-то itmathrepetitor опять тополя itmathrepetitor"
    print("Входная строка: ", my_str)
    arr = [i for i in my_str]  # все элементы строки
    res = func(arr)
    print('Результат:', ''.join(res))
