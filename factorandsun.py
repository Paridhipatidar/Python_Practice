a=int(input("Enter a positive integer:"))
print("Factors:",end=" ")
s=0
for i in range(1,a+1):
    if(a%i==0):
        print(i,end=" ")
        s=s+i
print("\nSum of factors:", s)    
