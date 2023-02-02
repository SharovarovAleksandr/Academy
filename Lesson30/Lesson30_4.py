import hashlib

def kolision(key,dc):
    return key.hexdigest() in dc.keys()

ls=["Any word","Any word","Any word ","Second word","Third word","Hello world!"]
dc=dict()
for i in ls:
    key=hashlib.md5(bytes(i, 'UTF-8'))
    while kolision(key,dc): # У випадку виникнення колізії до строки додається пробіл у кінці.
        print(i)
        i+=" "
        key = hashlib.md5(bytes(i, 'UTF-8'))
    dc[key.hexdigest()] = len(i)

print(dc)
