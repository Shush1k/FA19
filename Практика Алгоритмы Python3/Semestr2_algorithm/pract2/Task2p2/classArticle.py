from classIzdanieBook import Izdanie
class Article(Izdanie):
    def __init__(self, name, aut_name, journ_name, journ_num, journ_date):
        super().__init__(name, aut_name)
        self.journ_name = str(journ_name)
        self.journ_num = str(journ_num)
        self.journ_date = str(journ_date)

    def info(self):
        print("\n*Class СТАТЬЯ*\n")
        print("Название статьи:", self.name, "\nАвтор:", self.aut_name,
              "\nНазвание журнала:", self.journ_name, "\nНомер журнала:",
              self.journ_num, "\nГод издания:", self.journ_date)