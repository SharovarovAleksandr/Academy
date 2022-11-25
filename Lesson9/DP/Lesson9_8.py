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
    @property
    def data_access(self):
        return self.__data_access

    @user_mail.setter
    def user_mail(self,nikname):
        self.__user_mail=nikname
    @age.setter
    def age(self, howold):
        self.__age = howold
    @data_access.setter
    def data_access(self, howold):
        self.__data_access = howold

#Варіант 1 Через метод класу
    @classmethod
    def acs(cls,data_access):
        if data_access=="superuser" or data_access=="moderator":
            return "access granted"
        else:
            return "access denied"
#Варіант 2 Через метод екземпляру класу
    def acsexempl(self):
        if self.data_access == "superuser" or self.data_access == "moderator":
            return "access granted"
        else:
            return "access denied"

a=input("Введіть свій статус : ")

# Через метод класу
print(User.acs(a),"  Варіант 1 ")

# Через метод екземпляру класу
b=User("Vasya")
b.data_access=a
print(b.acsexempl(), "  Варіант 2")


