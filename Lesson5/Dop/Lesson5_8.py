import os

def way(name):
    return os.listdir(name)


str=input("Введіть шлях до каталогу: ")
print(way(str))