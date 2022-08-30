def findFactorialUptoN(n):
    x=1
    if n<0:
        return 0
    else:
        for i in range(1,n+1):
            a=x*i
            x=a
        return x


findFactorialUptoN(int(input("Enter Number")))