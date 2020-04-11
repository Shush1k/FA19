def palindrome(word):
    """Дано слово, состоящее только из строчных латинских букв. Проверьте, является ли это
    слово палиндромом. Выведите YES или NO. При решении этой задачи нельзя пользоваться
    циклами и нельзя использовать срезы с шагом, отличным от 1"""
    if len(word) == 0:
        return "Длина слова ноль"
    elif len(word) == 1:
        return "Yes"
    else:
        if word[0] == word[-1]:
            if len(word) == 2:
                return "Yes"
            return palindrome(word[1:-1])
        else:
            return "No"

    
word = input("Введите слово: ")
print("Вывод:", palindrome(word))