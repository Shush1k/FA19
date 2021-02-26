import os
import shutil
from pathlib import Path



#TODO:
# 1 Создание папки(с указанием имени)(mkdir) DONE
# 2 Удаление папки по имени (rm) DONE
# 3 Перемещение между папками (в пределах рабочей папки) - заход в папку по имени, выход на уровень вверх (cd) TODO
# 4 создание пустых файлов с указаным именем (touch) DONE
# 5 запись текста в файл DONE
# 6 просмотр содержимого текстового файла (cat) DONE
# 7 удаление файлов по имени (rm -r) DONE
# 8 копирование файлов из одной папку в другую (cp) DONE
# 9 перемещение файлов (mv) DONE
# 10 переименовывание файлов DONE

class FileManager:
    """
    Необходимо создать примитивный файловый менеджер. Программа должна работать в определенной папке (рабочей
    папке менеджера) и позволять пользователю выполнять следующие простые действия в пределах рабочей папки.

    @param path - путь к рабочей директории
    """
    def __init__(self, path):
        """
        @param self.PATH - абсолютный путь рабочей директории
        """
        self.PATH = Path(path).absolute()
        
        print("\nПуть к рабочей директории:\n"+str(self.PATH))
        try:
            os.chdir(self.PATH)
        except FileNotFoundError:
            print("Рабочая директория не найдена")
        self.currDir = self.PATH


    def createDir(self, path):
        """
        Задание 1 

        Создание папки по имени.
        @param path - имя папки.
        """
        if os.path.exists(path):
            print("Папка уже существует")
        else:
            os.mkdir(str(path))
    
    def deleteDir(self, path):
        """
        Задание 2 

        Удаление папки по имени.
        @param path - имя папки.
        """
        if os.path.exists(path):
            os.rmdir(str(path))
        else:
            print("Папки с таким именем не существует")

    def changeDir(self, path):
        """
        Задание 3 

        Перемещение между папками.
        @param path - путь к папке.
        TODO выход на уровень вверх, а также работа в пределах рабочей директории
        """ 
        try:
            os.chdir(path)
            self.currDir = self.PATH.joinpath(path)
            print("Перешли в папку:", self.currDir.name)
        except FileNotFoundError:
            print("Папки с таким именем не существует")
    
    def createFile(self, path):
        """
        Задание 4 

        Создание файла по имени.
        @param path - путь к файлу.
        """
        try:
            if os.path.exists(path):
                print("Файл уже существует")
            else:
                open(path, "w", encoding="utf-8").close()
        except FileNotFoundError:
            print("\nПуть к файлу не найден")

    def writeFile(self, path, text):
        """
        Задание 5 
        
        Запись в текстовый файл.
        @param path - путь к файлу.
        @param text - информация на запись в файл.
        """
        self.PATH.joinpath(path).write_text("tExt")

    def showFile(self, path):
        """
        Задание 6 

        Просмотр содержимого текстового файла.
        @param path - путь к файлу.
        """
        print(self.PATH.joinpath(path).read_text())
    


    def deleteFile(self, path):
        """
        Задание 7 

        Удаление файла по имени.
        @param path - путь к файлу.
        """
        if os.path.exists(path):
            os.remove(self.PATH.joinpath(path))
        else:
            print("Файла с таким именем не существует") 

    def copyFile(self, curr_path, new_path):
        """
        Задание 8

        Копирование файлов
        @param curr_path - путь откуда копируем
        @param new_path - путь куда копируем
        """
        if os.path.exists(curr_path):
            shutil.copy2(curr_path, new_path)
        else:
            print("Файла с таким именем не существует") 

    def moveFile(self, curr_path, new_path):
        """
        Задание 9

        Перемещение файлов
        @param curr_path - текущее расположение файла
        @param new_path - новое место файла
        """
        if os.path.exists(curr_path):
            os.replace(curr_path, new_path)
        else:
            print("Файла с таким именем не существует") 

    def renameFile(self, path, new_name):
        """
        Задание 10

        Переименование файла. (Пермещение файлов тоже работает, прям как в линухе)
        @param path - путь к файлу.
        @param new_name - новое имя файла.
        """
        if os.path.exists(path):
            self.PATH.joinpath(path).rename(new_name)
        else:
            print("Файла с таким именем не существует")


if __name__ == "__main__":
    f = FileManager("Test")
    # f.createDir("test1/test3")
    # f.deleteDir("test3")
    # f.createFile("test2/bbb")
    # f.renameFile("test1/www", "test2/www")
    # f.moveFile("test2/www", "test1/www")
    # f.deleteFile("www")
    # f.copyFile("test1/www", "test2/123") 