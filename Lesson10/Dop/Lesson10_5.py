def list_func(l,n):
    try:
        if n<0 and n>-len(l):
            print("Зверніть увагу що це елемент списку у зворотньому порядку.")
        return l[n]
    except IndexError:
        if n> len(l):
            print ("Елементу з таким номером немає у списку. ")
            return -1
        elif n<-len(l):
            print("Номер елементу списку є від'ємним числом яке більше за розмір списку.")
            return -1
    except TypeError:
            print("Номер елементу списку може бути тільки цілим числом.")
            return -1


a=[1,2,3,4,5,"Agh","f","ytf",12]

while True:
    try:
        n=int(input("Введіть номер елементу списку : "))
        print("Елемент ",n, "має значення", list_func(a,n))
        break
    except ValueError:
        print("Номер елементу списку може бути тільки цілим числом.")
    except Exception:
        print("Виникла непередбачувана помилка спробуйте ще раз. ")