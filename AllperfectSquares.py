import math
def AllperfectSquares(n):
    flag=False
    x=math.sqrt(n)
    m=round(x)
    if(m-x==0):
        flag=True
    return flag

def sumofsquare(n):
    sum1=0
    for i in range(1,n):
        if(AllperfectSquares(i)):
            print i
            sum1+=i

        print "sum of perfect squares",sum1
n=input("enter the number:")
print(sumofsquare(n))