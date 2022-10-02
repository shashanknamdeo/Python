
def subLists(list1):
    list2=[[]]
    for r in range(len(list1)+1):
        for i in range(r):
            list2.append(list1[i:r])
    return list2