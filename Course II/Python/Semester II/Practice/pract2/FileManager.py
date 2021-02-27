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
        @param self.PATH - рабочая директория
        """
        self.PATH = Path(path).absolute()
        self.last_dir = self.PATH.name
        
        print("\nПуть к рабочей директории:\n"+str(self.PATH))
        try:
            os.chdir(self.PATH)
        except FileNotFoundError:
            print("Рабочая директория не найдена")
        # Текущая директория
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
            try:
                os.mkdir(str(path))
                print("Создана папка", path.split("/")[-1])
            except FileNotFoundError:
                print("Указанный путь некорректный")
    
    def deleteDir(self, path):
        """
        Задание 2 

        Удаление папки по имени.
        @param path - имя папки.
        """
        if os.path.exists(path):
            shutil.rmtree(str(path))
            print("Удалена папка", path.split("/")[-1])
        else:
            print("Папки с таким именем не существует")

    def changeDir(self, path):
        """
        Задание 3 

        Перемещение между папками.
        @param path - путь к папке.
        """ 
        try:
            if path == "..":
                if self.last_dir in str(self.currDir.parent):
                    os.chdir(self.currDir.parent)
                    self.currDir = self.PATH.joinpath(self.currDir.parent)
                    print("Текущий путь:", self.currDir)
                else:
                    print("Выход за пределы рабочей директории невозможен!")
                    
            else:
                os.chdir(path)
                self.currDir = self.PATH.joinpath(path)
                print("Текущий путь:", self.currDir)
            
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
        try:
            self.currDir.joinpath(path).write_text(text)
        except FileNotFoundError:
            print("Файл не найден")

    def showFile(self, path):
        """
        Задание 6 

        Просмотр содержимого текстового файла.
        @param path - путь к файлу.
        """
        if os.path.exists(path):
            print(self.currDir.joinpath(path).read_text())
        else:
            print("Файла с таким именем не существует") 


    def deleteFile(self, path):
        """
        Задание 7 

        Удаление файла по имени.
        @param path - путь к файлу.
        """
        if os.path.exists(path):
            os.remove(self.currDir.joinpath(path))
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
        try:
            if os.path.exists(path):
                self.currDir.joinpath(path).rename(new_name)
            else:
                print("Файла с таким именем не существует")
        except FileExistsError:
            print("Файл уже существует")


if __name__ == "__main__":
    # Если запускать, то лучше по частям
    f = FileManager("Test")
    # первая часть
    # f.createDir("test1")
    # f.createDir("test1/guide")
    # f.createDir("test2")
    # f.createFile("test2/bbb")
    # f.renameFile("test2/bbb", "test2/www")
    # f.writeFile("test1/www", "Hello, FileManager!")
    # f.moveFile("test1/www", "test2/www")
    # f.copyFile("test2/www", "test1/www_in_test1") 
    # f.showFile("test1/www_in_test1")
    # f.deleteFile("test2/www")
    # # вторая часть
    # f.changeDir("test1/guide")
    # f.changeDir("..")
    # f.changeDir("..")
    # f.changeDir("..")
    # f.deleteDir("test1")
    # f.deleteDir("test2")