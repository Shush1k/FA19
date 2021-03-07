from FileManager import FileManager
from config import FM_PATH


f = FileManager(FM_PATH)
f.info()
print("\nПуть рабочей директории:", f.getCurrDir())
print(str("_"*100)+"\n")
while True:
    choice = input("==> ")
    if choice == "createDir" or choice == "1":
        print("Создание папки")
        dirname = input("Введите название папки: ")
        f.createDir(dirname)

    elif choice == "deleteDir" or choice == "2":
        print("Удаление папки")
        dirname = input("Введите название папки: ")
        f.deleteDir(dirname)

    elif choice == "changeDir" or choice == "3":
        print("Перемещение в папку")
        dirname = input("Введите путь к директории: ")
        f.changeDir(dirname)

    elif choice == "createFile" or choice == "4":
        print("Создание файла")
        filename = input("Название файла: ")
        f.createFile(filename)

    elif choice == "writeFile" or choice == "5":
        print("Запись в файл")
        filename = input("Название файла: ")
        text = input("Текст: ")
        f.writeFile(filename, text)

    elif choice == "showFile" or choice == "6":
        print("Просмотр файла")
        filename = input("Название файла: ")
        f.showFile(filename)

    elif choice == "deleteFile" or choice == "7":
        print("Удалить файл")
        filename = input("Название файла: ")
        f.deleteFile(filename)

    elif choice == "copyFile" or choice == "8":
        print("Скопировать файл")
        currpath = input("Название файла: ")
        newpath = input("Скопировать в: ")
        f.copyFile(currpath, newpath)

    elif choice == "moveFile" or choice == "9":
        print("Переместить файл")
        currpath = input("Название файла: ")
        newpath = input("Переместить в: ")
        f.moveFile(currpath, newpath)

    elif choice == "renameFile" or choice == "10":
        print("Переименовать файл")
        filepath = input("Название файла: ")
        newname = input("Переименовать в: ")
        f.renameFile(filepath, newname)

    elif choice == "tree" or choice == "11":
        print("Дерево директорий:")
        f.showTree(f.currDir)

    elif choice == "showCD" or choice == "12":
        print("Текущий путь:", f.getCurrDir())

    elif choice == "info" or choice == "help" or choice == "?":
        f.info()

    elif choice == "exit" or choice == "0":
        print("Bye")
        break
