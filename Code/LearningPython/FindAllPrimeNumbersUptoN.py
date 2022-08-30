def toCheakPrimeNumber(number):
    for val in range(2,number):
        if number%val==0:
            return False
    return True

x=int(input("Enter Number"))

for i in range(2,x+1):
    if toCheakPrimeNumber(number=i)==True:
        print(i) 