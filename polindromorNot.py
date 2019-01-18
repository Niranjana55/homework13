def polindromorNot(n):
    flag="is polindrom"
    num=n
    revnum=0
    while(n>0):
        temp=n%10
        revnum=revnum*10+temp
        n=n//10
    if not(revnum==num):
        flag="is not a polindrom"
    return flag

n=input("enter the number:")
print(polindromorNot(n))