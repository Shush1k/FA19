import classIzdanieBook
class Web(classIzdanieBook.Izdanie):
    def __init__(self, name, aut_name, link, annotation):
        super().__init__(name, aut_name)
        self.link = str(link)
        self.annotation = str(annotation)

    def info(self):
        print("\n*Class ЭЛЕКТРОННЫЙ РЕСУРС*\n")
        print("Название статьи:", self.name, "\nАвтор:", self.aut_name,
              "\nСсылка:", self.link, "\nАннотация:",
              self.annotation)