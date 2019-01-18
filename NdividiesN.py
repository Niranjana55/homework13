def NdividiesN(n):
    flag=True
    num=n
    while(n>0):
        temp=n%10
        if(num%temp==0):
            flag=True
        else:
            flag=False
        n=n/10
    return flag

n=input("Enter the number:")
print(NdividiesN(n))
        
