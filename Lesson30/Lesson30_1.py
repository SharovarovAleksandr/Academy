import hashlib
class Hasher_Tab():

    def __init__(self,tab={},len=None):
        if isinstance(tab,dict):
            if tab:
                n=0
                for i in tab:
                    tab[i] = hashlib.md5(bytes(str(i), "UTF-8"))
                    n+=1
                self.tab=tab
                self.len = n
            else:
                self.tab={None:None}
                self.len=0
        else:
            print("Argument of class must be dictionary!")

    def __str__(self):
        try:
            print("Hasher_Tab object number of components ",self.len)
            if self.len!=0:
                for i in self.tab:
                    print(i,":",self.tab[i].hexdigest())
            else:
                print("None:None")
        except:
            print("Hasher_Tab object has ERROR OF CREATION")
        return ""

    def create(n):
        dc=dict()
        for i in range(n):
            dc[i]=i
        return Hasher_Tab(dc)

    def add(self,new):
        nw=hashlib.md5(bytes(str(new.partition(":")[2]),"UTF-8"))
        self.tab[new.partition(":")[0]]=nw
        self.len+=1
        return self

    def add_key(self,new_key):
        if new_key in self.tab.keys():
            print("Component  with this key",new_key," already exists")
        else:
            self.tab[new_key] =hashlib.md5(bytes(str(None),"UTF-8"))
            self.len+=1
        return self

    def write_hash(self,key,new):
        new1=hashlib.md5(bytes(str(new),"UTF-8"))
        for i in self.tab:
            if self.tab[i].hexdigest()==new1.hexdigest():
                print("Component  with this value", new, " already exists")
                return self
        if key in self.tab.keys():
            self.tab[key]=hashlib.md5(bytes(str(new), "UTF-8"))
        else:
            st=str(key)+":"+str(new)
            self.add(st)
        return self

    def del_tab(self,key):
        if key in self.tab.keys():
            self.tab.pop(key)
            self.len-=1
        return self

    def find_key(self,key):
        if key in self.tab.keys():
            return str(key)+":"+str(self.tab[key].hexdigest())
        else:
            return "Key "+str(key)+" not found"

    def find_value(self,value):
        value1 = hashlib.md5(bytes(str(value), "UTF-8"))
        for i in self.tab:
            if self.tab[i].hexdigest() == value1.hexdigest():
                return (value,value1.hexdigest())
        return None

a=Hasher_Tab.create(3)
print(a)
dc={1:23,2:65,7:75}
a=Hasher_Tab(dc)
b=a.add("23:23")
b=a.add_key(75)
b=a.write_hash(35,35)
b=a.del_tab("35")
b=a.write_hash(35,35)
print(a)
print(a.find_key(1))
print(a.find_value(23))
