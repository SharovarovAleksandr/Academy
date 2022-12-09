# Формуємо бінарну купу
import random
from binarytree import *

def inp(n):
	j=0
	while j<2:
		print("Enter number less then", n, end="  ")
		try:
			x=int(input())
		except TypeError:
			continue
		else:
			if x>n:
				print("Number more then", n)
			else:
				if j==0:
					l=x
				else:
					r=x
				j+=1
	return l,r

def inp_rand(n,max=100):
	r=random.randint(0,n)
	l=random.randint(0,n)
	return l,r

def gen_tr(h,r,aut):
	j=1
	while j<h+1:
		st=int(2**(j-1)-1)
		en=int(2**j-1)
		for i in range(st,en):
			if aut=="Y":
				a,b=inp_rand(ls[i],max)
				ls.append(a)
				ls.append(b)
			else:
				a, b = inp(ls[i])
				ls.append(a)
				ls.append(b)
		j+=1
	return ls

ls=[]
max=100
h=int(input("Height of Binary heap : "))
if h<=0:
	print("Такого дерева не існує! ")
else:
	r = int(input("Root of Binary heap   : "))
	ls.append(r)
	aut=input("Create Binary heap automatically (Y/N) ")
	if aut=="Y":
		max =int(input("MAX node value in Binary heap : "))
	ls=gen_tr(h,r,aut)
print(ls)
t=build(ls)
print(t)
print(t.properties)


t3=heap(h)
print(t3)
print(t3.properties)