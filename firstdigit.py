def firstdigit(n):
    while(n>0):
        n=n//10
    return n
n=input("enter the number:")
print(firstdigit(n))