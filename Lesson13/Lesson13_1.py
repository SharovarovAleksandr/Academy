import time
import random
from random_words import RandomWords

def rand_int(n,start,end):
    l=[]
    for i in range(n):
        l.append(random.randint(start,end))
    return l

def rand_float(n,start,end):
    l=[]
    for i in range(n):
        l.append(random.uniform(0.1,100))
    return l


w=RandomWords()
int_list=rand_int(5000,0,1000)
print(int_list)
float_list=rand_float(5000,0,1000)
print(float_list)
str_list=w.random_words(letter=None,count=5000, min_letter_count=3)
print(str_list)