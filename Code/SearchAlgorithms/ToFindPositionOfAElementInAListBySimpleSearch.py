def positionOfElementInList(x,list1):
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




list0 = input("Enter List")
element = input("Enter Element")
positionOfElementInList(element,list0)


