import hashlib
dic_pass=dict()
ps=input('Ви вже зареєстрований користувач? (Y/N)')
if ps!="Y":
    with open('dic_pass.psw', 'r+', encoding="utf8") as fl_psw:
        ls = fl_psw.readlines()
        for i in ls:
            dic_pass[i.partition(":")[0]] = i.partition(":")[2][:-1]
        while True:
            name=input("Введіть ім`я для реєстрації в системі : ")
            if name in dic_pass.keys():
                print("Користувач з таким ім'ям вже є в системі. Спробуйте ввести інше ім'я.")
            else:
                break
        while True:
            passwd=input('Введіть пароль для реєстрації в системі : ')
            hash_passwd = hashlib.md5(bytes(passwd, "UTF-8"))
            if hash_passwd in dic_pass.values():
                print("Цей пароль вже зайнятий Спробуйте новий пароль.")
            else:
                break
        ls=name+":"+hash_passwd.hexdigest()+'\n'
        fl_psw.write(ls)

with open('dic_pass.psw', 'r', encoding="utf8") as fl_psw:
    ls = fl_psw.readlines()
    for i in ls:
        dic_pass[i.partition(":")[0]] = i.partition(":")[2][:-1]
    while True:
        name=input("Введіть Ваше ім`я : ")
        if name in dic_pass.keys():
            break
        else:
            print("У мене немає зареєстрованого користувача із таким ім'ям. Спробуйте ще.")
    while True:
        passwd=input('Введіть пароль для входу в систему : ')
        hash_passwd = hashlib.md5(bytes(passwd, "UTF-8"))
        if hash_passwd.hexdigest() in dic_pass.values() and dic_pass[name]==hash_passwd.hexdigest():
            print("Ви авторизовані. Чекаю на ваші розпорядження!")
            break
        else:
            print("У мене немає зареєстрованого користувача із таким паролем. Спробуйте ще.")

    print("Починаємо сеанс роботи!")