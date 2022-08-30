

def toMakeBlockOfNxN(x):
    if x%y==0:
        return True
    else:
        return False


val=int(input('enter nmber'))
y=val**0.5

for i in range(1,val+1):
    if toMakeBlockOfNxN(x=i)==True:
        print()
    elif toMakeBlockOfNxN(x=1)==False:
        print(1,end='')

# -----------------------------------------------------------------------------


number = int(input('Enter Number'))
for i in range(0, int(number**0.5)+1):
    for i in range(0, int(number**0.5)+1):
        print(1, end = '')
    print()



number = int(input('Enter Number'))
for i in range(0, int(number**0.5)+1):
    for j in range(0, int(number**0.5)+1):
        print(i*10+j+1, end = '')
    print()