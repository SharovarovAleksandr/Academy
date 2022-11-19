class Drone(object):
    def __init__(self,model,enginnum,camtype):
        self.model=model
        self.enginnum=enginnum
        self.camtype=camtype

    @classmethod
    def takeoff(cls):
        speed=int(input("З якою швидкістю злітаємо :"))
        return "Зліт на швидкості : ", speed

    @classmethod
    def landing(cls,speed):
        return "Сідати будемо на швидкості - ", speed



Drone.model=input("Введіть модель безпилотника : ")
Drone.enginnum=int(input("Введіть кількість двигунів :"))
Drone.camtype="CamType1"
c=input("Введіть Зліт/Посадка :")
if c=="Зліт":
    d=Drone.takeoff()
elif c=="Посадка":
    a = int(input(" На якій скорості будемо сідати? "))
    d=Drone.landing(a)
else:
    d="Мені здається ви зовсім не пілот!"
print(d)
print(Drone.model)
print(Drone.enginnum)
print(Drone.camtype)

