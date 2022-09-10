def toCheckEvenOrOdd(val):
    if val%2 == 0:
        return 0
    else:
        return 1


def binarysearch(list1,x):
    list2=[]
    import math
    a1=math.ceil(math.sqrt(len(list1)))
    if len(list1)==1:
        val=1 
    elif list1[0]==x:
        return 1
    elif x>list1[0]:
        low=0
        high=len(list1)-1
        val=-1
        for r in range (0,a1):
            mi=high+low
            mit=high-low
            mid=mi//2
            mi1=mi+1
            mi2=mi-1
            mid1=mi1//2
            mid2=mi2//2
            list2.append(mid)
            if toCheckEvenOrOdd(mit)==0:
            ## number of element from low to high is odd
                if list1[mid] == x:
                    val=mid
                    list2.append(mid)
                elif list1[mid+1] <= x:
                    low = mid+1
                elif list1[mid-1] >= x:
                    high = mid-1
            elif toCheckEvenOrOdd(mit)==1:
                if list1[mid1] < x:
                    low=mid1
                elif list1[mid1] > x:
                    high=mid1
                elif list1[mid1]==x:
                    list2.append(mid1)
    temp=len(list2)-1
    return list2[temp]+1


##list input not suported
