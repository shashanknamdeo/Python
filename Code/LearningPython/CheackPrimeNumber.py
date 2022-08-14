val=input("Enter Number")
val=int(val)

prime_flag = True
for n in range(2,val):
    if val%n==0:
        prime_flag = False
        break

if prime_flag == True:
    print(val,'is prime')
else:
    print(val,'is not prime')



def cheakPrimeNumber(number_to_chake):
    for n in range(2,number_to_chake):
        if number_to_chake%n==0:
            return False
    return True