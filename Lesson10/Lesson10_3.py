# Порахувати суму елементів списку, якщо у списку виникає елемент словник то в сумму добавити сумму числових елементів items словника
class MyErr(Exception):
    def __init__(self,*args):
        if args:
            self.message= args[0]
        else:
            self.message=None

    def __str__(self):
        if self.message:
            return 'MyErr ,{0}'.format(self.message)
        else:
            return 'MyErr has been raised!'

    def fix(d):
        s=0
        for i in d:
            if isinstance(d[i],int) or isinstance(d[i],float):
                s=s+d[i]
        return s


def sum(a):
    s=0
    for i in a:
        try:
            if isinstance(i,dict):
                raise MyErr
            else:
                s=s+i
        except TypeError:
            print("Виникла помилка невідповідності типів даних")
        except MyErr:
            s=s+MyErr.fix(i)
        except Exception as e:
            print("Виникла непередбачувана помилка ",e)
        else:
            continue
    return s



a=[1,2,3,45,12.3,{1:"Січень",2:"Лютий",3:"Березень",4:13.5},-12.2,{5:"Травень",6:15,7:28,8:35,9:"Вересень",10:"Жовтень",11:"Листопад",12:"Грудень"},4,8]
print(sum(a))