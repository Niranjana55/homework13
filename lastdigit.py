def lastdigit(n):
    temp=0
    while(n>0):
        temp=n%10
        return temp
n=input("enter the number:")
print(lastdigit(n))