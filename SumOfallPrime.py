import math
def SumOfallPrime(n):
    a=True
    if(n==1):
        return False
    if(n==2):
        return True
    for i in range(2,int(math.sqrt(n)+1)):
        if(n%i==0):
            a=False
    return a

def toprintprime(n):
    sum1=0
    for i in range(2,n+1):
        if(SumOfallPrime(i)):
            print i
            sum1+=i

    print "sum of prime numbers",sum1
n=input("enter the number:")
print(toprintprime(int(n)))