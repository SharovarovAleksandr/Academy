def my_f(*args):
    for i in args:
        if type(i)!=str :
            return False
        else:
            continue
    return True


print(my_f(1,2,3,"ghj","hjk"))
print(my_f("hj","gjk","tre"))
