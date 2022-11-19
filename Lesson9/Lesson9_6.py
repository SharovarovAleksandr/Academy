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

#User.user_mail="test@gmail.com"
#a=User("Vasja","test@gmail.com",35,"Male",3)
a=User("Vasya")
print(a.user_mail)
#User.age=35

print(a.user_name)
print(User.user_mail)
print(a.age)



