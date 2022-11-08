
def nam(n1):
    f=open(n1,"r",encoding="utf8")
    a=list(f.read())
    if a.count(":")==0:    # Перевірка чи може ця послідовність бути словником
        print("Файл не містить елементів словника ")
        return

    num1 = a.count(" ")    # Ця операція  прибирає всі зайві пробіли
    for i in range(num1):  # вона  не обов'язкова,
        a.remove(" ")      # залежить від формату вхідного файлу

    if a[-1]!="\n":        # не обов'язковий оператор залежить від формату файлу
        a+="\n"

    d=dict()
    while len(a)>1:
        s1 = ""
        s2 = ""
        num2 = a.index(":")
        num3 = a.index("\n")
        for i in range(num2):
            s1 += a[i]
        for i in range(num2+1,num3):
            s2+=a[i]
        for i in range(num3+1):
            a.remove(a[0])
        d.update({s1:s2})
    return d

n=input("Введіть ім'я файлу: ")
print(nam(n))

