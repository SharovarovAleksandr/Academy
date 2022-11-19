def square(a,b):
    return a*b


while True:
    try:
        a = int(input("Введіть довжину сторони a прямокутника : "))
        if a<=0:
            raise KeyError
        break
    except ValueError:
        print("Сторона прямокутника може бути тільки  числом. ")
    except KeyError:
        print("Довжина сторони не може бути менше чи дорівнювати 0 ")
    except Exception:
        print("Виникла непередбачувана помилка спробуйте ще раз. ")
while True:
    try:
        b = int(input("Введіть довжину сторони b прямокутника : "))
        if b<=0:
            raise KeyError
        if a==b:
            print ("Зверніть увагу що ваш прямокутник -  квадрат!!!")
        break
    except ValueError:
        print("Сторона прямокутника може бути тільки  числом. ")
    except KeyError:
        print("Довжина сторони не може бути менше чи дорівнювати 0 ")
    except Exception:
        print("Виникла непередбачувана помилка спробуйте ще раз. ")

print("Площа вашого прямокутника = ",square(a,b))
