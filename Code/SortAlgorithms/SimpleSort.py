def simpleSort(input_list):
    """first i deside to put (value_of_temp=)input_list[0] as smallest element
        then 1 i find is there any element less than input_list[0]
        if i find it then i put it in value_of_temp and search and find is there any element less than it
        by doing it i get smallest valve in list
        then i put it at first position and put 1st position value at small value position

        theni deside to put (value_of_temp=)input_list[1] as smallest element
        then 1 i find is there any element less than input_list[2]
        if i find it then i put it in value_of_temp and search and find is there any element less than it
        by doing it i get second smallest valve in list
        then i put it at 2nd position and put 2nd position value at 2nd small value position
        and repeat it with input_list[3],input_list[4],etc
        and i get sorted list
        
        example
        list1 = [4,5,3,1,-9]
        simpleSort(list1)
        list1 = [-9,1,3,4,5]
    """
    for i in range(0,len(input_list)):
        value_of_temp = input_list[i]
        position_of_temp=i
        for n in range(i, len(input_list)):
            if input_list[n] < value_of_temp:
                value_of_temp = input_list[n]
                position_of_temp = n
        value_of_i_position=input_list[i]
        input_list[i]=value_of_temp
        input_list[position_of_temp]=value_of_i_position
    return input_list


list1 = [input("Enter List Elements: ")]
toSortNumbers(_list)


