# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import sys
import shutil


def make_dir():
    print('Текущая директория: ', os.getcwd())
    i = 1
    while i < 10:
        try:
            dir_name = (os.path.join(os.getcwd(), 'dir_{}'.format(i)))
            os.mkdir(dir_name, 777)
        except:
            print('Папка', 'dir_{}'.format(i), 'уже существует')
        i += 1
    else:
        print('Все папки созданы')


def del_dir():
    i = 1
    while i < 10:
        dir_name = (os.path.join(os.getcwd(), 'dir_{}'.format(i)))
        os.rmdir(dir_name)
        i += 1
    else:
        print('Все лишнее удалено')


# make_dir()
# del_dir()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def view_dir():
    for el in os.listdir(os.getcwd()):
        if os.path.isdir(os.getcwd() + '\\' + el):  # Проверяем является ли объект папкой
            print(el)


# view_dir()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file():
    shutil.copy('hw05-easy.py', 'hw05-easy_copy.py')

# copy_file()