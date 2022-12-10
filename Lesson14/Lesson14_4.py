# Формуємо бінарне дерево
import random
from binarytree import *
def inp(n):
	while True:
		print("Enter number less then", n, end="  ")
		l=input()
		if l=="":
			l=None
			break
		else:
			l=int(l)
			if l>n:
				print("Number more then", n)
			else:
				break
	while True:
		print("Enter number more then", n, end="  ")
		r=input()
		if r == "":
			r = None
			break
		else:
			r = int(r)
			if r<n:
				print("Number less then", n)
			else:
				break
	return l,r

def inp_rand(n,max=100):
	r=random.randint(n,max)
	l=random.randint(0,n)
	if l==0 or l==n:
		l=None
	elif r==max or r==n:
		r=None
	return l,r

def gen_tr(h,r,aut):
	j=1
	while j<h+1:
		st=int(2**(j-1)-1)
		en=int(2**j-1)
		for i in range(st,en):
			if ls[i]==None:
				ls.append(None)
				ls.append(None)
			else:
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
h=int(input("Height of tree : "))
if h<=0:
	print("Такого дерева не існує! ")
else:
	r = int(input("Root of tree   : "))
	ls.append(r)
	aut=input("Create BST automatically (Y/N) ")
	if aut=="Y":
		max =int(input("MAX node value in BST : "))
	ls=gen_tr(h,r,aut)
	print(ls)
t=build(ls)
print(t.is_bst)
print(t)
print(t.properties)


t1=bst(h,is_perfect=True)
print(t1)
print(t1.properties)
l=t1.values
print(l)

# t3=heap(h)
# print(t3)
# print(t3.properties)