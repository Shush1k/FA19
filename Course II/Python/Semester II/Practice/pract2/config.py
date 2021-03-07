from FileManager import FileManager
from pathlib import Path
"""
Файл настроек
"""
#MY_PATH Рабочая папка FileManager
MY_PATH = "Home"
#FM_PATH Рабочая директория FileManager
FM_PATH = Path(MY_PATH).absolute()


# проверка команд
# if __name__ == "__main__":
    # Если запускать, то лучше по частям
    # f = FileManager("Test")
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