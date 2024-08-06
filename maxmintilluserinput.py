i=0 
max=0
min=99999
while True:
    a=input("you wanna enter num ")
    if a=="no":
        break
    else:
        b=int(input("enter a num"))
        if(b>max):
            max=b
        if(b<min):
            min=b
        i=i+1    
print("max=",max)
print("min=",min)