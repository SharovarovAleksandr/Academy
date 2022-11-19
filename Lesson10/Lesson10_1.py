
def month(n):
    a={1:"Січень",2:"Лютий",3:"Березень",4:"Квітень",5:"Травень",6:"Червень",7:"Липень",8:"Серпень",9:"Вересень",10:"Жовтень",11:"Листопад",12:"Грудень"}
    if isinstance(n,bool) or isinstance(n,list) or isinstance(n,tuple):
        print("Номер місяця не може бути логічною змінною, списком або кортежем")
        return True
    try:
        if n in range(1,12) and isinstance(n,int):
            print("Зараз місяць -", a[n])
        elif isinstance(n,float):
            print("Ви ввели данні типу Float. ")
            raise ValueError
        elif isinstance(n,str) and n in str(a.keys()):
            n=int(n)
            print("Зараз місяць -", a[n])
            return False
        elif isinstance(n,str) and (not (n in str(a.keys()))):
            raise KeyError
        else:
            raise ValueError
    except ValueError as e1:
        print("Номер місяця ціле число яке не може бути меншим 1 та більшим 12!")
        return True
    except KeyError as e2:
        if isinstance(n,str):
            print("Ви ввели некоректні строкові данні. ")
            return True
    except TypeError as e3:
        print("Виникла помилка із невідповідністю типів даних!",e3)
        return True
    except Exception as e4:
        print("Номер місяця ціле число яке не може бути меншим 1 та більшим 12!",e4)
        return True
    else:
        return False

def vvod():
    return input("Ще раз введіть номер місяця: ")


a = input("Введіть номер місяця: ")
#a=12.5
#a=True
#a=list()
#a=tuple()
while month(a):
    a=vvod()
print(" Гарного дня!")

