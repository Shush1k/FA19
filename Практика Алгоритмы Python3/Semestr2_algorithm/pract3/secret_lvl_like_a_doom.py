def hell_circles(n = 99):
    """Так пропадают пираты, которые пиратят хорошие игры с торрента"""
    #песен я не нашел!
    if n == 0:
        return yellow_text("А теперь все на дне!")
    else:
        print("Ууу " + str(n) + " пиратос на корабле!")
        green_text("А теперь на дне ещё один")
        red_text("Бум и все по новой\n")
        return hell_circles(n-1)
    
def input_N():
    """Ввод числа N"""
    try:
        N = int(input("Всего пиратов: "))
        return N
    except ValueError:
        print("Вводить число!")
        return input_N()
        
def yellow_text(text):
    print("\033[33m"+str(text)+"\033[0m")

def green_text(text):
    print("\033[32m"+str(text)+"\033[0m")
    
def red_text(text):
    print("\033[31m"+str(text)+"\033[0m")


hell_circles(input_N())