num=int(input("enter a positive num"))
c=0
for i in range(1,num+1):
    if(num%i==0):
        c=c+1
if(c==2):
    print("prime")
else:
    print(" not prime")