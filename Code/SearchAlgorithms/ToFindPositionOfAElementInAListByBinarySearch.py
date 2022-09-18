def toCheckEvenOrOdd(val):
    if val%2 == 0:
        return 0
    else:
        return 1

def binarySearch(given_list, element):
    """
    given_list=[r for r in range(1,101)]
    binarySearch(given_list=given_list, element=51)
    """
    low=0
    high=len(given_list)-1
    while (high-low)>0:
        number_of_element_from_low_to_high=high-low+1
        mid_for_odd_element_list=(high+low)//2
        mid_for_even_element_list_high=(high+low+1)//2
        mid_for_even_element_list_low=(high+low-1)//2
        if toCheckEvenOrOdd(number_of_element_from_low_to_high)==1:
            ## number of element from low to high is odd
            if element == given_list[mid_for_odd_element_list]:
                return mid_for_odd_element_list
            elif element >= given_list[mid_for_odd_element_list+1] :
                low = mid_for_odd_element_list+1
            elif element <= given_list[mid_for_odd_element_list-1] :
                high = mid_for_odd_element_list-1
            else:
                return -1
        elif toCheckEvenOrOdd(number_of_element_from_low_to_high)==0:
            ## number of element from low to high is even
            if element <= given_list[mid_for_even_element_list_low]:
                high = mid_for_even_element_list_low
            elif element >= given_list[mid_for_even_element_list_high]:
                low = mid_for_even_element_list_high
            else:
                return -1
    if given_list[low] == element:
        return low
    else :
        return -1