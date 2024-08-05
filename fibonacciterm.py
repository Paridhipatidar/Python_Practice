num=int(input("enter num of terms"))
n1=0
n2=1
n3=0
print(n1,n2,end=" ")
for i in range(2,num):
    n3=n1+n2
    print(n3,end=" ")
    n1=n2
    n2=n3

