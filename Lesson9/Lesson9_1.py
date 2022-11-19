class Auto(object):
    def __init__(self,model,colour,v_engine):
        self.model=model
        self.colour = colour
        self.v_engin=v_engine

    def forward(self):
        return "Поїхали уперед. "

    def back(self):
        return "Давно казав, що потрідно вертатися. "

class NewCar(Auto):
    def left(self):
        return "Поїхали ліворуч "

    def right(self):
        return "Поїхали праворуч. "

print("Оберіть назву машини ")
a = Auto("Kia", "Red", 1800)
print(a.model, a.colour, a.v_engin)
b=NewCar("BMW","Black",2490)
print(b.model, b.colour, b.v_engin)

while True:
    d = input("Оберіть марку машини ")
    if d==a.model or d==b.model:
        break
    else:
        print("У нас немає такої машини. Спробуйте ще раз. ")
        continue

c = input("What direction? ")
if c == "forward":
    print(b.forward())
elif c == "back":
    print(b.back())
elif c=="left" and d==b.model:
    print(b.left())
elif c=="right" and d==b.model:
    print(b.right())
else:
    print("Я туди не поїду!")
