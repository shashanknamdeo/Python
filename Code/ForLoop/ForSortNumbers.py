def toSortNumbers(_list):
    """
    """
    sorted_list = []
    for i in range(0,len(_list)):
        temp = _list[0]
        for n in range(0, len(_list)):
            if temp > _list[n]:
                temp = _list[n]
        _list.remove(temp)
        sorted_list.append(temp)
    # 
    return sorted_list

x = [input('enter')]

_list = [4,5,3,1,-9]


_list = [input("Enter List Elements: ")]
toSortNumbers(_list)