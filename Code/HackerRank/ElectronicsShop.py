"""
A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a give budget. Given price lists for keyboards and USB drives and a budget, find the cost to buy them. If it is not possible to buy both items, return .

Example



The person can buy a , or a . Choose the latter as the more expensive option and return .

Function Description

Complete the getMoneySpent function in the editor below.

getMoneySpent has the following parameter(s):

int keyboards[n]: the keyboard prices
int drives[m]: the drive prices
int b: the budget
Returns

int: the maximum that can be spent, or  if it is not possible to buy both items
Input Format

The first line contains three space-separated integers , , and , the budget, the number of keyboard models and the number of USB drive models.
The second line contains  space-separated integers , the prices of each keyboard model.
The third line contains  space-separated integers , the prices of the USB drives.

Constraints

The price of each item is in the inclusive range .
Sample Input 0

10 2 3
3 1
5 2 8
Sample Output 0

9
Explanation 0

Buy the  keyboard and the  USB drive for a total cost of .

Sample Input 1

5 1 1
4
5
Sample Output 1def pickingNumbers(a):
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

-1
Explanation 1

There is no way to buy one keyboard and one USB drive because , so return .
"""

def getMoneySpent(keyboards, drives, b):
    price=[]
    for k_price in keyboards:
        for d_price in drives:
            total_price = k_price+d_price
            if total_price <= b:
                price.append(total_price)
    #
    if len(price)==0:
        return -1
    temp_price=price[0]
    for element in price:
        if element > temp_price :
            temp_price = element
    return temp_price