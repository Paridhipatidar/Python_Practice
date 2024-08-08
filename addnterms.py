import math
term=int(input("enter num of terms"))
sum=0
for i in range(1,term+1):
    sum= sum+i/math.factorial(i)
print(sum)