## only for sorted list
def toCheckEvenOrOdd(val):
    if val%2 == 0:
        return even
    else:
        return odd

def linearSearch(x,list1):
    for i in range(0,len(list1)):
        if list1[i] == x:
            temp == 1
            return i
        else:
            temp = 0
    if temp == 1:
        return i +1
    elif temp == 0:
        return "element not present"

def positionOfElementInList(list1,x):
    temp = len(list1)/2
    if toCheckEvenOrOdd(len(list1)) == odd :
        if list(temp-0.5) > x :
            linearSearch(x,list1)