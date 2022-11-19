import random
num=random.randint(1,100)
b=True
for i in range(1,7):
    while True:
        try:
            n = int(input("Введіть число : "))
            if n<1 or n>100:
                raise ValueError
            break
        except ValueError:
            print("Число може бути тільки  від 1 до 100.")
        except Exception:
            print("Виникла непередбачувана помилка спробуйте ще раз. ")
    if n==num:
        print("Вітаю ви вгадали число ",num,"  Кількість спроб",i)
        b=False
        break
    elif n>num:
        print("Мое число менше ")
    elif n<num:
        print("Моє число більше")
if b:
    print("Вибачте ви програли")
