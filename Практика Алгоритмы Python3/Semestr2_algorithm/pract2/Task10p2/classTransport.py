class Transport:
    def __init__(self, mark, coordinate):
        self.mark = mark
        self.coordinate = coordinate

    def info(self):
        print("\n*Class ТРАНСПОРТ*\n")
        print("Марка:", self.mark, "\nКоординаты:", self.coords_to_str())

    def Coord_func(self, coord_list):
        y_list, x_list = coord_list
        y1, y2 = y_list
        x1, x2 = x_list

        locale_x, locale_y = self.coordinate

        if x1 <= locale_x <= x2 and y1 <= locale_y <= y2:
            return True
        return False

    def coords_to_str(self):
        x, y = self.coordinate
        return "["+str(x)+", "+str(y)+"]"