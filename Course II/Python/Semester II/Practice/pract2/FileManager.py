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
        try:
            os.chdir(self.PATH)
        except FileNotFoundError:
            print("Рабочая директория не найдена")
        # Текущая директория
        self.currDir = self.PATH

    def getCurrDir(self):
        return self.currDir

    def createDir(self, path):
        """
        Задание 1 

        Создание папки по имени.
        @param path - имя папки.
        """
        try:
            if os.path.exists(path):
                print("Папка уже существует")
            else:
                os.makedirs(str(path))
                print("Создана папка", path.split("/")[-1])
        except FileNotFoundError:
            print("Указанный путь некорректный")
        except OSError:
            pass
    
    def deleteDir(self, path):
        """
        Задание 2 

        Удаление папки по имени.
        @param path - имя папки.
        """
        # try:
        if os.path.isdir(path):
            shutil.rmtree(str(path), ignore_errors=True)
            if str(path) == ".":
                print("Содержимое текущей папки удалено")
            else:
                print("Удалена папка", path.split("/")[-1])
        else:
            print("Папки с таким именем не существует")
        # except PermissionError:
        #     pass
            

    def changeDir(self, path):
        """
        Задание 3 

        Перемещение между папками.
        @param path - путь к папке.
        """ 
        try:
            if len(path) != 0:
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
        except OSError:
            pass
    
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
        except OSError:
            pass

    def writeFile(self, path, text):
        """
        Задание 5 
        
        Запись в текстовый файл.
        @param path - путь к файлу.
        @param text - информация на запись в файл.
        """
        try:
            self.currDir.joinpath(path).write_text(text)
            print(f"Создан файл: {path}\nСодержимое файла: {text}")
        except FileNotFoundError:
            print("Файл не найден")
        except OSError:
            pass

    def showFile(self, path):
        """
        Задание 6 

        Просмотр содержимого текстового файла.
        @param path - путь к файлу.
        """
        try:
            if os.path.exists(path):
                print("=="*10 +"\n"+ str(self.currDir.joinpath(path).read_text()) +"\n"+ "=="*10)
            else:
                print("Файла с таким именем не существует") 
        except OSError:
            pass

    def deleteFile(self, path):
        """
        Задание 7 

        Удаление файла по имени.
        @param path - путь к файлу.
        """
        try:
            if os.path.exists(path):
                os.remove(self.currDir.joinpath(path))
                print(f"Файл {path} удален!")
            else:
                print("Файла с таким именем не существует")
        except OSError:
            print("Файла с таким именем не существует") 

    def copyFile(self, curr_path, new_path):
        """
        Задание 8

        Копирование файлов
        @param curr_path - путь откуда копируем
        @param new_path - путь куда копируем
        """
        try:
            if os.path.exists(curr_path):
                shutil.copy2(curr_path, new_path)
                print(f"Файл скопирован в {new_path}")
            else:
                print("Файла с таким именем не существует")
        except OSError:
            print("Файла с таким именем не существует") 

    def moveFile(self, curr_path, new_path):
        """
        Задание 9

        Перемещение файлов
        @param curr_path - текущее расположение файла
        @param new_path - новое место файла
        """
        try:
            if os.path.exists(curr_path):
                os.replace(curr_path, new_path)
                print(f"Файл перемещен из {curr_path} в {new_path}")
            else:
                print("Файла с таким именем не существует")
        except OSError:
            pass


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
                print(f"Файл переименован в {new_name}")
            else:
                print("Файла с таким именем не существует")
        except FileExistsError:
            print("Файл уже существует")
        except OSError:
            print("Файла с таким именем не существует") 

    def showTree(self, path):
        """
        Показ структуры папки
        """
        tree = os.walk(path)
        for i in tree:
            print(i[0])



    def info(self):
        """
        Справка по командам FileManager
        """
        print(str("=-" * 30)+"=")
        print("                     FileManager Menu\n")
        print("0.   exit        Выход из FileManager")
        print("1.   createDir   Создание папки(с указанием имени)")
        print("2.   deleteDir   Удаление папки по имени")
        print("3.   changeDir   Перемещение между папками")
        print("4.   createFile  Создание пустых файлов с указаным именем")
        print("5.   writeFile   Запись текста в файл")
        print("6.   showFile    Просмотр содержимого текстового файла")
        print("7.   deleteFile  Удаление файлов по имени")
        print("8.   copyFile    Копирование файлов из одной папку в другую")
        print("9.   moveFile    Перемещение файлов")
        print("10.  renameFile  Переименовывание файлов")
        print("11.  tree        Показать дерево директорий")
        print("12.  showCD      Узнать текущую директорию")
        print("13.  info        Справка")

        print(str("=-" * 30)+"=")