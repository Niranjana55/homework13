def oddnumbers(n):
    sum1=0
    for i in range(1,n*2,2):
        print i
        sum1+=i
    print sum1
n=input("enter the number:")
oddnumbers(n)