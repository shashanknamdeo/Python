"""
Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to .

Example


There are two subarrays meeting the criterion:  and . The maximum length subarray has  elements.

Function Description

Complete the pickingNumbers function in the editor below.

pickingNumbers has the following parameter(s):

int a[n]: an array of integers
Returns

int: the length of the longest subarray that meets the criterion
Input Format

The first line contains a single integer , the size of the array .
The second line contains  space-separated integers, each an .

Constraints

The answer will be .
Sample Input 0

6
4 6 5 3 3 1
Sample Output 0

3
Explanation 0

We choose the following multiset of integers from the array: . Each pair in the multiset has an absolute difference  (i.e.,  and ), so we print the number of chosen integers, , as our answer.

Sample Input 1

6
1 2 2 3 1 2
Sample Output 1

5
Explanation 1

We choose the following multiset of integers from the array: . Each pair in the multiset has an absolute difference  (i.e., , , and ), so we print the number of chosen integers, , as our answer.
"""
def pickingNumbers(a):
    n=len(a)
    a.sort()
    
    def findIndex(keyList, key):
        for i in range(len(keyList)):
            if(keyList[i] == key):
                return i
    keyList = []
    valueList = []
    count = 1
    for idx in range(0, n):
        if(a[idx] not in keyList):
            keyList.append(a[idx])
            valueList.append(1)
        elif(a[idx] in keyList):
            index = findIndex(keyList, a[idx])
            valueList[index] += 1
    #print(keyList)
    #print(valueList)
    #max of just one case
    max_val =  max(valueList)
    for i in range(1, len(keyList)):
        pairCount = 0
        if(keyList[i]-keyList[i-1] <= 1):
            pairCount = valueList[i]+valueList[i-1]
        
        if(max_val < pairCount):
            max_val = pairCount
    print(max_val)




_________________________________________________________________________

"""
wrong thinking 
think than we have to pick number which are in longest series os less tha or equal to 1
example  [1,2,2,4,1,2,2,3]
we have to pick 1,2,2,1,2,2,3 

"""

0 1 1 2 0 1
x 0 0 1 1 0
x x 0 1 1 0
x x x 0 2 1
x x x x 0 1
x x x x x 0


1 2 2 3 1 2

matrix
1: x 1 1 2 0 1  -> [1,2,4,5]
2: x x 0 1 1 0  -> [2,3,4,5]
2: x x x 1 1 0  -> [3,4,5]
3: x x x x 2 1  -> [5]
1: x x x x x 1  -> [5]
2: x x x x x x  -> > NULL

for row in matrix:
    for col in row:

NxN

-> 1 2 2 3 2
-> 1 2 2 1 2
-> 1 2 2 2
-> 1 2 1
-> 1 2 2