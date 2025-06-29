"""
This code gives  maximum no. of element in which maximum difference is less than 1 and grater than -1

example 1
list1=[1,5,2,8,4,3,2,1,8]
a=pickingNumbers(list1)
a=4

   explaination
   4,3,2,1  is longest set in which maximum difference is less than 1 and grater than -1

example 2
list2=[1,6,3,4,4,5,6,6,5,4,2,8]
b=pickingNumbers(list2)
b=8

   explaination
   3,4,4,5,6,6,5,4  is longest set in which maximum difference is less than 1 and grater than -1
"""
def toGetModulusOfANumber(x):
    if x < 0:
        y = -1*x
        return y
    else :
        return x


def pickingNumbers(a):
    list1=[]
    no_of_continous_integer=1
    for i in range(0,len(a)):
        if i<=len(a)-2:
            if toGetModulusOfANumber((a[i]-a[i+1])) <= 1:
                temp_no_of_continous_integer=no_of_continous_integer+1
                no_of_continous_integer=temp_no_of_continous_integer
            else :
                list1.append(no_of_continous_integer)
                no_of_continous_integer=1
        else :
            list1.append(no_of_continous_integer)
            no_of_continous_integer=1
    if len(list1)==0:
        return 1
    else:
        temp_no_of_integer=list1[0]
        for element in list1:
            if element > temp_no_of_integer :
                temp_no_of_integer = element
        return temp_no_of_integer



