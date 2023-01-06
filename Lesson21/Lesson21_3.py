import numpy as np

a=np.array([[7,0,8,8,8],
            [0,0,1,3,5],
            [0,0,0,-3,5],
            [0,0,0,0,0,],
            [0,0,0,0,0]])
print(a*4)

b=np.array([[2,1],
            [-3,0],
            [4,-1]])

c=np.array([[5,-1,6],
            [-3,0,7]])
print(b.dot(c))

d=np.array([1,2,3])
e=np.array([[4],[5],[6]])
e1=np.array([4,5,6])
print(d)
print(e)
print(e1)
print(d.dot(e),d.dot(e1))
