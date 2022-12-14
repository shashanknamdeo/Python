"""
You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

The first kangaroo starts at location  and moves at a rate of  meters per jump.
The second kangaroo starts at location  and moves at a rate of  meters per jump.
You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO.

Example




After one jump, they are both at , (, ), so the answer is YES.

Function Description

Complete the function kangaroo in the editor below.

kangaroo has the following parameter(s):

int x1, int v1: starting position and jump distance for kangaroo 1
int x2, int v2: starting position and jump distance for kangaroo 2
Returns

string: either YES or NO
Input Format

A single line of four space-separated integers denoting the respective values of , , , and .

Constraints

Sample Input 0

0 3 4 2
Sample Output 0

YES
Explanation 0

The two kangaroos jump through the following sequence of locations:

image

From the image, it is clear that the kangaroos meet at the same location (number  on the number line) after same number of jumps ( jumps), and we print YES.

Sample Input 1

0 2 5 3
Sample Output 1

NO
Explanation 1

The second kangaroo has a starting location that is ahead (further to the right) of the first kangaroo's starting location (i.e., ). Because the second kangaroo moves at a faster rate (meaning ) and is already ahead of the first kangaroo, the first kangaroo will never be able to catch up. Thus, we print NO.

Language
Python 3

More
67891011121314151617181920212223242526272829303132333435363738394041
Line: 41 Col: 1

Submit Code

Run Code

Upload Code as File

Test against custom input
"""
def toCheckInteger(n):
    import math
    a = math.floor(n)
    b = n/a
    if b == 1.0:
        # n is integer
        return 0
    else:
        # n is non integer
        return 1

def kangaroo(x1, v1, x2, v2):
    if v1 != v2:
        j=(x1-x2)/(v2-v1)
        if j >= 1 :
            if toCheckInteger(j) == 0:
                return 'YES'
            else:
                return 'NO'
        else:
            return 'NO'
    else:
        return 'NO'