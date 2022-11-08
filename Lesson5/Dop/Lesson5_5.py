def last_line(name,col):
    f = open(name, "r", encoding="utf8")
    s=list(f.readlines())
    n=len(s)
    if col>=n:
        print ("Файл місить тільки ",n," рядків ось вони:")
        for i in range(n):
            print(s[i], end="")
    else:
        for i in range(n-col,n):
            print(s[i],end="")



str = input("Введіть шлях до файлу: ")
n=int(input("Скільки останніх рядків зчитувати? "))
last_line(str,n)
