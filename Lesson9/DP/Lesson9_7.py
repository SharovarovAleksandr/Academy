class User(object):
    def __init__(self,user_name,user_mail="test",age=0,user_type="",data_access=""):
        self.user_name=user_name
        self.__user_mail=user_mail
        self.__age=age
        self.__user_type=user_type
        self.__data_access=data_access
    @property
    def user_mail(self):
        return self.__user_mail
    @property
    def age(self):
        return self.__age

    @user_mail.setter
    def user_mail(self,nikname):
        self.__user_mail=nikname
    @age.setter
    def age(self, howold):
        self.__age = howold

# Варіант 1 З використанням аргументу класу
    def vik():
        if User.age>=18 and User.age<=60:
            return "Eligable"
        else:
            return "NonEligable"

# Вариант 2 використання статичної функції класу із незалежним аргументом
    @staticmethod
    def vik1(old):
        if old>=18 and old<=60:
            return "Eligable"
        else:
            return "NonEligable"

a=int(input("Введіть вік користувача: "))
User.age=a
print(User.vik()," Віриант 1")
print(User.vik1(a)," Віриант 2")


