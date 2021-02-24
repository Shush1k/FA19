import os
from pathlib import Path



#TODO:
# 1 Создание папки(с указанием имени)(mkdir) DONE
# 2 Удаление папки по имени (rm) DONE
# 3 Перемещение между папками (в пределах рабочей папки) - заход в папку по имени, выход на уровень вверх (cd)
# 4 создание пустых файлов с указаным именем (touch) DONE
# 5 запись текста в файл
# 6 просмотр содержимого текстового файла (cat)
# 7 удаление файлов по имени (rm -r) DONE
# 8 копирование файлов из одной папку в другую (cp)
# 9 перемещение файлов (mv)
# 10 переименовывание файлов DONE

class FileManager:
    """
    Необходимо создать примитивный файловый менеджер. Программа должна работать в определенной папке (рабочей
    папке менеджера) и позволять пользователю выполнять следующие простые действия в пределах рабочей папки.
    """
    def __init__(self, path):
        self._files = {}
        self.PATH = Path(path).absolute()
        print("\nПуть к папке\n",self.PATH)
        try:
            os.chdir(self.PATH)
        except FileNotFoundError:
            print("Рабочая директория не найдена")


    def createDir(self, dir_name):
        """
        Задание 1

        Создание папки по имени.
        @param dir_name - имя папки.
        """
        if os.path.exists(dir_name):
            print("Папка уже существует")
        else:
            os.mkdir(str(dir_name))
    
    def deleteDir(self, dir_name):
        """
        Задание 2

        Удаление папки по имени.
        @param dir_name - имя папки.
        """
        if os.path.exists(dir_name):
            os.rmdir(str(dir_name))
        else:
            print("Папки с таким именем не существует")

    def changeDir(self, part_path):
        """
        Задание 3 НЕ РАБОТАЕТ

        Перемещение между папками.
        @param part_path - путь к папке.
        """
        path = Path(part_path).absolute()
        if not path.is_dir():
            print("Путь не является папкой")
        else:
            try:
                os.chdir(path.name)
                print("Перешли в папку:", path.name)
            except FileNotFoundError:
                print("Папки с таким именем не существует")
    
    def createFile(self, file_name):
        """
        Задание 4

        Создание файла по имени.
        @param file_name - имя файла.
        """
        if os.path.exists(file_name):
            print("Файл уже существует")
        else:
            open(file_name, "w", encoding="utf-8").close()

    def deleteFile(self, file_name):
        """
        Задание 7

        Удаление файла по имени.
        @param file_name - имя папки.
        """
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("Файла с таким именем не существует") 

    def renameFile(self, file_name, new_file):
        """
        Задание 10

        Переименование файла.
        @param file_name - имя файла.
        @param new_file - новое имя файла.
        """
        if os.path.exists(file_name):
            os.rename(file_name, new_file)
        else:
            print("Файла с таким именем не существует")


if __name__ == "__main__":
    f = FileManager("Test")
    # f.createDir("test1")
    # f.deleteDir("test1")
    # f.createFile("bbb")
    # f.renameFile("bbb", "www")
    # f.deleteFile("www")
    f.changeDir("test1")
