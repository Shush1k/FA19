from FileManager import FileManager


f = FileManager("Test")
f.info()
print("\nПуть рабочей директории:", f.getCurrDir())
print(str("_"*100)+"\n")
while True:
    choice = input("==> ")
    if choice == "createDir" or choice == "1":
        dirname = input("Создание папки: ")
        f.createDir(dirname)

    elif choice == "deleteDir" or choice == "2":
        dirname = input("Удаление папки: ")
        f.deleteDir(dirname)

    elif choice == "changeDir" or choice == "3":
        dirname = input("Перемещение в папку: ")
        f.changeDir(dirname)

    elif choice == "createFile" or choice == "4":
        filename = input("Создание файла: ")
        f.createFile(filename)

    elif choice == "writeFile" or choice == "5":
        filepath = input("Запись в файл: ")
        text = input("Текст: ")
        f.writeFile(filepath, text)

    elif choice == "showFile" or choice == "6":
        filename = input("Просмотр файла: ")
        f.showFile(filename)

    elif choice == "deleteFile" or choice == "7":
        filename = input("Удалить файл: ")
        f.deleteFile(filename)

    elif choice == "copyFile" or choice == "8":
        currpath = input("Скопировать файл: ")
        newpath = input("Скопировать в: ")
        f.copyFile(currpath, newpath)

    elif choice == "moveFile" or choice == "9":
        currpath = input("Переместить файл: ")
        newpath = input("Переместить в: ")
        f.moveFile(currpath, newpath)

    elif choice == "renameFile" or choice == "10":
        filepath = input("Переименовать файл: ")
        newname = input("Переименовать в: ")
        f.renameFile(filepath, newname)

    elif choice == "info" or choice == "help" or choice == "?":
        f.info()

    elif choice == "exit" or choice == "0":
        print("Bye")
        break