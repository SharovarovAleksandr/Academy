class MyData():
    a = [0, 0, 1, 2, 3, 3, "A", "B", "C", "C", True, True, False, 12.5, 13.3, 14.0, 14.0, (1, 2, "FG",True, 3, 4), (1, True, 2), (1, 2),
         [1, 2], [1, 2, 3], [1,(True,"jf",[48,73,False,(56,67)],32), 2]]
    b=[]


class MyError(Exception):
    def __init__(self,arg):
        self.arg= arg

    # Рекурсивная функція proces(a,b) перевіряє список a у якому повинні міститися тільки данні типу float або int.
    # У разі, якщо у списку зустрічаються змінні типу str це викликає помилку MyError(1) данні такого типу видаляються.
    # Якщо у списку зустрічаються змінні типу bool це викликає помилку MyError(2) данні такого типу замінюються - True на 1, False на 0.
    # Змінні типу list та Tuple викликають помилку MyError(3) та MyError(4) відповідно та перетворюються у послідовний список,
    # якщо ці вложені змінні містять данні типу str або bool вони також оброблюються відповідно до алгоритму. Кількість вложених
    # списків та кортежей обмежується тільки можливістю рекурсивного  звернення до функції.
    # В результаті ми отримуємо список b який містить виключно послідовність чисел

    def proces(a,b):
        n1=len(a)
        for i in a:
            try:
                if isinstance(i,str):
                    c=MyError(1)
                    raise MyError(1)
                elif isinstance(i,bool):
                    c=MyError(2)
                    raise MyError(2)
                elif isinstance(i,tuple):
                    c=MyError(3)
                    raise MyError(3)
                elif isinstance(i,list):
                    c=MyError(4)
                    raise MyError(4)
                else:
                    b.append(i)
            except MyError :
                if c.arg==1:
                    continue
                elif c.arg==2:
                    if i:
                        b.append(1)
                    else:
                        b.append(0)
                elif c.arg==3 or 4:
                    b.extend(i)
            except TypeError as e1:
                print(" У списку є непередбачені види данних ",e1)
        n2=len(b)
        if n1==n2:

# Питання до викладача!
# Шановний Вікторе Володимировичу!
# Чому при виконанні оператора return b функція не повертає список b а дає відповідь що вона None?
# Для вирішення цієї проблеми скористався "костилем" MyData.b=b хоча це не правильно

            MyData.b=b
            return b
        else:
            a=b
            b=[]
            MyError.proces(a,b)



a=MyData.a
b=[]
print(a)
с=MyError.proces(a,b) # Намагався по різному але результат все одно None
print(с)
print(MyData.b) # Тільки при використанні змінної іншого класу повертається коректна відповідь
print(" Унікальні числа у списку : ",set(MyData.b))
