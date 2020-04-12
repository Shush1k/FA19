import math
def equation(self):
    x = self.x
    if x<=0 or ((1-math.log(x))<0) or x>2:
        print("Не подходит по ОДЗ")
    else:
        y=x**3/((x+1)*(x+2)) + (math.asin(1-x))/pow((1-math.log(x)),1/3)
        print("y=",y)            