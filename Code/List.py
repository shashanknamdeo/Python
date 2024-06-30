sublist_list = []

def sublists(lst, index=0, current=[]):
    """
    sublists(lst=[0,1,2,3])
    """
    # print(lst, index, current)
    if index == len(lst):
        sublist_list.append(current)
        return
    sublists(lst, index+1, current)
    sublists(lst, index+1, current + [lst[index]])