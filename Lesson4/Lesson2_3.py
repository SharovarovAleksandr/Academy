import statistics
numbers=[1,8,5,4,12]

#First method
print("First method")
print("The mean is =",statistics.mean(numbers))


#Second method
s=int(0)
n=len(numbers)
for i in range(n):
    s=s+int(numbers[i])
mean_s=s/n
print("Second method")
print("The mean is = ",mean_s)

