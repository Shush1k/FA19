class Izdanie:
    def __init__(self, name, aut_name):
        self.name = str(name).title()
        self.aut_name = str(aut_name)

    def info(self):
        print("\n*Class ИЗДАНИЕ*\n")
        print("Название книги:", self.name, "\nАвтор:", self.aut_name)

class Book(Izdanie):
    def __init__(self, name, aut_name, date, place_izd):
        super().__init__(name, aut_name)
        self.date = str(date)
        self.place_izd = str(place_izd)

    def info(self):
        print("\n*Class КНИГА*\n")
        print("Название книги:", self.name, "\nАвтор:", self.aut_name,
              "\nГод издания:", self.date, "\nИздательство:", self.place_izd)