class Parallelogram(object):
    def __init__(self,width,length):
        self.width=width
        self.length=length

    def get_area(self):
        return self.width*self.length

class Square(Parallelogram):
    def __init__(self,len):
        self.len=len

    def get_area(self):
        return self.len*self.len


a=Parallelogram(10,20)
print(a.width,a.length)
print(a.get_area())
a= Square(50)
print(a.len)
print(a.get_area())

