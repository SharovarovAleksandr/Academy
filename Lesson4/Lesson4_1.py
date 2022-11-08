def month(a):
    if a<=0 or a>12:
        return "Немає такого місяця"
    elif a>=3 and a<=5:
        return "Весна на дворі"
    elif a>=6 and a<=8:
        return "Вітаю із літом"
    elif a>=9 and a<=11:
        return "Осінь прийшла"
    else:
        return "І знову зима"

i=int(input("Введіть номер місяця: "))
print(month(i))

