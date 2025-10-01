
# def implementTwoStacksinOneArray():
#     """
#     n = given length of array
#     unable to use OPPs concept to implement
#     https://www.geeksforgeeks.org/dsa/implement-two-stacks-in-an-array/
#     """
#     array = [None]*n
#     pointer_1 = -1
#     pointer_1 = len(array)
#     def push1(value):
#         """
#         """
#         if pointer_1 + 1 < pointer_2:
#             array[pointer_1] = value
#             pointer_1 += 1
#         else:
#             print("Stack-1-is-full")
#     # 
#     # 
#     def push2(value):
#         """
#         """
#         if pointer_2 - 1 > pointer_1:
#             array[pointer_1] = value
#             pointer_1 -= 1
#         else:
#             print("Stack-2-is-full")
#     # 
#     # 
#     def pop1():
#         """
#         """
#         if pointer_1 > -1:
#             pointer_1 -= 1
#             return interval_array[pointer_1 + 1]
#         else:
#             print("Stack-1-is-empty")
#             return -1
#     # 
#     # 
#     def pop2():
#         """
#         """
#         if pointer_1 < len(array):
#             pointer_1 += 1
#             return interval_array[pointer_1 - 1]
#         else:
#             print("Stack-2-is-empty")
#             return -1

# # -------------------------------------------------------------------------------------------------

# def evaluationOfPostfixExpression(array):
#     """
#     """
#     stack = []
#     # 
#     for item in array:
#         if item.isdigit():
#             stack.append(int(item))
#         else:
#             val1 = stack.pop()
#             val2 = stack.pop()
#             # 
#             if item == "+":
#                 stack.append(val2 + val1)
#             elif item == "-":
#                 stack.append(val2 - val1)
#             elif item == "*":
#                 stack.append(val2 * val1)
#             elif item == "/":
#                 stack.append(val2 / val1)
#         # 
#     return stack.pop()

# # -------------------------------------------------------------------------------------------------

# class MyStack(object):
#     """
#     """
#     def __init__(self):
#         print('__init__')
#         self.queue_1 = []
#         self.queue_2 = []
#         self.front_queue = self.queue_1
#         self.back_queue = self.queue_2
#     # 
#     def push(self, x):
#         print('push')
#         self.front_queue.append(x)
#     # 
#     def pop(self):
#         print('pop')
#         if not self.front_queue:
#             return None
#         # 
#         while len(self.front_queue) > 1:
#             self.back_queue.append(self.front_queue.pop(0))
#         # 
#         self.front_queue, self.back_queue = self.back_queue, self.front_queue
#         return self.back_queue.pop(0)
#     # 
#     def top(self):
#         print('top')
#         if not self.front_queue:
#             return None
#         # 
#         while len(self.front_queue) > 1:
#             self.back_queue.append(self.front_queue.pop(0))
#         # 
#         self.front_queue, self.back_queue = self.back_queue, self.front_queue
#         self.top_int = self.back_queue.pop(0)
#         self.front_queue.append(self.top_int)
#         print(self.front_queue, self.back_queue, self.top_int)
#         return self.top_int
#     # 
#     def empty(self):
#         print('empty')
#         if not self.front_queue:
#             return True
#         else:
#             return False

# # -------------------------------------------------------------------------------------------------

# def reverseQueue(self, queue):
#     """
#     """
#     stack = []
#     while not queue.empty():
#         stack.append(queue.get())
#     # 
#     for _ in range(len(stack)):
#         queue.put(stack.pop())
#     # 
#     return queue

# # -------------------------------------------------------------------------------------------------

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None

# class Deque:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#     # 
#     def insert_first(self,data):
#         new_node = Node(data)
#         # 
#         if self.head == None:
#             self.head = self.tail = new_node
#         # 
#         else:
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node
#     # 
#     def insert_last(self,data):
#         new_node = Node(data)
#         # 
#         if self.tail == None:
#             self.tail = self.head = new_node
#         else:
#             new_node.prev = self.tail
#             self.tail.next = new_node
#             self.tail = new_node
#     # 
#     def isEmpty(self):
#         if (self.head == None) and (self.tail == None):
#             return True
#         else:
#             return False
#     # 
#     def size(self):
#         if self.isEmpty():
#             return 0
#         else:
#             node = self.head
#             size = 1
#             while node.next != None:
#                 size += 1
#                 node = node.next
#             # 
#             return size
#     # 
#     def remove_first(self):
#         if self.isEmpty():
#             print('Deque is empty')
#             return None
#         # 
#         data = self.head.data
#         # 
#         if self.head == self.tail:  # only one element
#             self.head = self.tail = None
#         else:
#             self.head = self.head.next
#             self.head.prev = None
#         # 
#         return data
#     # 
#     def remove_last(self):
#         if self.isEmpty():
#             print('Deque is empty')
#             return None
#         # 
#         data = self.tail.data
#         # 
#         if self.head == self.tail:  # only one element
#             self.head = self.tail = None
#         else:
#             self.tail = self.tail.prev
#             self.tail.next = None
#         # 
#         return data
#     # 
#     def display(self):
#         elements = []
#         node = self.head
#         # 
#         while node:              # traverse until None
#             elements.append(node.data)
#             node = node.next
#         # 
#         return elements


# class Stack:
#     def __init__(self):
#         self.stack = Deque()
#     # 
#     def push(self,data):
#         self.stack.insert_last(data)
#     # 
#     def pop(self):
#         return self.stack.remove_last()
#     # 
#     def size(self):
#         return self.stack.size()
#     # 
#     def display(self):
#         return self.stack.display()


# class Queue:
#     def __init__(self):
#         self.queue = Deque()
#     # 
#     def enqueue(self,data):
#         self.queue.insert_last(data)
#     # 
#     def dequeue(self):
#         return self.queue.remove_first()
#     # 
#     def size(self):
#         return self.queue.size()
#     # 
#     def display(self):
#         return self.queue.display()

# # -------------------------------------------------------------------------------------------------

# def reverseFirstK(self, queue, k):
#     """
#     Only following standard operations are allowed on queue.
#         enqueue(x) : Add an item x to rear of queue
#         dequeue() : Remove an item from front of queue
#         size() : Returns number of elements in queue.
#         front() : Finds front item.
#     """
#     size = queue.size()
#     if k > size:
#         return queue
#     # 
#     stack = deque()
#     for i in range(k):
#         stack.append(queue.dequeue())
#     # 
#     for i in range(k):
#         queue.enqueue(stack.pop())
#     # 
#     for i in range(size - k):
#         queue.enqueue(queue.dequeue())
#     # 
#     return queue

# # -------------------------------------------------------------------------------------------------

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None

# class Stack:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.mid  = None
#         self.size = 0
#     # 
#     def push(self, x):
#         new_node = Node(x)
#         self.size += 1
#         # 
#         if self.head == None:
#             self.head = self.tail = self.mid = new_node
#         else:
#             self.tail.next = new_node
#             new_node.prev = self.tail
#             self.tail = self.tail.next
#             # 
#             if self.size % 2 == 0:
#                 self.mid = self.mid.next
#     # 
#     def pop(self):
#         if self.tail == None:
#             print('Stack is Empty')
#             return None
#         # 
#         data = self.tail.data
#         self.size -= 1
#         if self.size == 0:
#             self.head = self.tail = self.mid = None
#         else:
#             self.tail = self.tail.prev
#             self.tail.next = None
#             # 
#             if self.size % 2 == 1:
#                 self.mid = self.mid.prev
#         # 
#         return data
#     # 
#     def findMiddle(self):
#         return self.mid.data
#     # 
#     def deleteMiddle(self):
#         if self.size == 0:
#             print('Stack is Empty')
#             return None
#         # 
#         self.size -= 1
#         data = self.mid.data
#         # 
#         if self.size == 0:
#             # 
#             self.head = None
#             self.tail = None
#             self.mid  = None
#         # 
#         elif self.size == 1:
#             self.tail = self.head
#             self.mid  = self.head
#             self.head.next = self.head.prev = None
#         # 
#         else:
#             prev_node =  self.mid.prev
#             next_node = self.mid.next
#             # 
#             prev_node.next = next_node
#             next_node.prev = prev_node
#             # 
#             if self.size % 2 == 1:
#                 self.mid = prev_node
#             else :
#                 self.mid = next_node
#         # 
#         return data


# # -------------------------------------------------------------------------------------------------


# def precedence(self, op):
#     if op == '^':
#         return 3
#     elif op in ('*', '/'):
#         return 2
#     elif op in ('+', '-'):
#         return 1
#     return 0

# def is_right_associative(self, op):
#     return op == '^'

# def infixtoPostfix(self, expr):
#     result = []
#     stack = []
#     # 
#     for ch in expr:
#         if ch.isalnum():  # operand
#             result.append(ch)
#         # 
#         elif ch == '(':
#             stack.append(ch)
#         # 
#         elif ch == ')':
#             while stack and stack[-1] != '(':
#                 result.append(stack.pop())
#             stack.pop()
#         # 
#         else:  # operator
#             while (stack and stack[-1] != '(' and
#                    (self.precedence(stack[-1]) > self.precedence(ch) or
#                     (self.precedence(stack[-1]) == self.precedence(ch) and not self.is_right_associative(ch)))):
#                 result.append(stack.pop())
#             stack.append(ch)
#     # 
#     while stack:
#         result.append(stack.pop())
#     # 
#     return "".join(result)


# -------------------------------------------------------------------------------------------------


def maxLength(string):
    max_result = 0
    stack = [-1]
    # 
    for i in range(len(string)):
        print(stack, max_result)
        if string[i] == '(':
            stack.append(i)
        # 
        elif string[i] == ')':
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_result = max(max_result, i - stack[-1])
    # 
    return max_result


# -------------------------------------------------------------------------------------------------

# Special stack

def push(arr, ele):
    if len(arr) == 0:
        global min_stack 
        min_stack = [ele]
    else:
        min_stack.append(min(ele, min_stack[-1]))
    arr.append(ele)


def pop(arr):
    if not arr:  # stack empty
        return -1   # GFG expects -1 when stack is empty
    min_stack.pop()
    return arr.pop()


# function should return 1/0 or True/False
def isFull(n, arr):
    if len(arr) == n:
        return True
    return False


# function should return 1/0 or True/False
def isEmpty(arr):
    return len(arr) == 0


# function should return minimum element from the stack
def getMin(n, arr):
    if not arr:
        return -1
    return min_stack[-1]


# -------------------------------------------------------------------------------------------------


def findDuplicateparenthesis(string):
    print(string)
    stack = ['#']
    flag = False
    for char in string:
        if flag == False:
            if char != ')':
                stack.append(char)
            else:
                while stack[-1] != '(':
                    stack.pop()
                # 
                stack.pop()
                if stack[-1] == '(':
                    flag = True
                    continue
        elif flag == True :
            if char == ')':
                return True
            else:
                flag = False
                stack.append(char)
    # 
    return False


# -------------------------------------------------------------------------------------------------


def validateOp(a, b):
    """
    """
    print(a, b)
    len_a = len(a)
    len_b = len(b)
    if len_a != len_b:
        return False
    # 
    stack = ['temp_ele']
    index_b = 0
    index_a = 0
    while index_b < len_b:
        print(stack, b[index_b])
        if stack[-1] == b[index_b]:
            stack.pop()
            index_b += 1
        else:
            if a and index_a < len_a:
                stack.append(a[index_a])
                index_a += 1
            else:
                return False
    # 
    return True


# -------------------------------------------------------------------------------------------------


def countNumber(n):
    """
    Count natural numbers whose all permutation are greater than that number
    # 
    approach 1 : simple
    approach 2 : deficult to understand
    """

# -------------------------------------------------------------------------------------------------

def sortStack(stack):
    """
    """
    if not stack:
        return stack
    # 
    temp = stack.pop()
    # 
    stack = sortStack(stack)
    # 
    stack = insertTemp(stack, temp)
    # 
    return stack


def insertTemp(stack, item):
    """
    """
    if not stack or stack[-1] <= item:
        stack.append(item)
        return stack
    # 
    temp = stack.pop()
    stack = insertTemp(stack, item)
    stack.append(temp)
    return stack

# -------------------------------------------------------------------------------------------------

from collections import defaultdict

def FirstNonRepeating(string):
    """
    """
    if not string:
        return string
    # 
    final_string = string[0]
    queue = [string[0]]
    # 
    char_dict = defaultdict(int)
    char_dict[string[0]] = 1
    # 
    print(string)
    for char in string[1:]:
        print(queue, char_dict, char_dict)
        if queue and queue[0] == char:
            queue.pop(0)
            while queue and char_dict[queue[0]] > 1:
                queue.pop(0)
                print('while : ', queue)
        # 
        if char_dict[char] == 0:
            queue.append(char)
            char_dict[char] += 1
        # 
        elif char_dict[char] == 1:
            char_dict[char] += 1
        # 
        final_string += queue[0] if queue else '#'
    # 
    return final_string

# -------------------------------------------------------------------------------------------------

def celebrity(matrix):
        size = len(matrix)
        index_list = []
        # 
        for i in range(0, size):
            if sum(matrix[i]) == 1:
                index_list.append(i)
        # 
        if not index_list:
            return -1
        # 
        for i in list(index_list):
            print('index_list 1 : ', i)
            celebrity = True
            for row in matrix:
                if row[i] == 0:
                    index_list.pop(0)
                    celebrity = False
                    print('celebrity False: ', i)
                    break
            if celebrity:
                print('celebrity True: ', i)
                break
            # 
        print('index_list 2 : ', index_list)
        return index_list[0] if index_list else -1

# -------------------------------------------------------------------------------------------------

def nextLargerElement(self, array):
    """
    Find the next greater element for each element in array.
    If no greater element exists, return -1 for that position.
    """
    n = len(array)
    if n == 0:
        return []
    # 
    result = [-1] * n   # default answer is -1
    stack = []          # will store indices
    # 
    # Traverse from right to left
    for i in range(n - 1, -1, -1):
        # Pop elements from stack which are <= current element
        while stack and stack[-1] <= array[i]:
            stack.pop()
        # 
        # If stack not empty, top is the next greater element
        if stack:
            result[i] = stack[-1]
        # 
        # Push current element onto stack
        stack.append(array[i])
    # 
    return result

# -------------------------------------------------------------------------------------------------

def nearest(self, grid):
    """
    https://www.geeksforgeeks.org/problems/distance-of-nearest-cell-having-1-1587115620/1
    Graph, Dynamic Programing, Matrix, Queue
    """

# -------------------------------------------------------------------------------------------------


def nextSmallerEle(self, array):
    """
    Find the next greater element for each element in array.
    If no greater element exists, return -1 for that position.
    """
    n = len(array)
    if n == 0:
        return []
    # 
    result = [-1] * n   # default answer is -1
    stack = []          # will store indices
    # 
    # Traverse from right to left
    for i in range(n - 1, -1, -1):
        # Pop elements from stack which are <= current element
        while stack and stack[-1] >= array[i]:
            stack.pop()
        # 
        # If stack not empty, top is the next greater element
        if stack:
            result[i] = stack[-1]
        # 
        # Push current element onto stack
        stack.append(array[i])
    # 
    return result

# -------------------------------------------------------------------------------------------------


def startStation(gas, cost):
    """
    def startStation(self, gas, cost):
    """
    len_station = len(gas)
    # 
    j = 0
    while j < len_station:
        fuel_tank = 0
        response = True
        for i in range(j, len_station):
            fuel_tank = gas[i] + fuel_tank - cost[i]
            # 
            if fuel_tank < 0:
                j = i + 1
                response = False
                break
        # 
        if response == True:
            for i in range(0, j):
                fuel_tank = gas[i] + fuel_tank - cost[i]
                # 
                if fuel_tank < 0:
                    j += 1
                    response = False
                    break
        # 
        if response == True:
            return j
    # 
    return -1

# -------------------------------------------------------------------------------------------------


class kStacks:
    # 
    def __init__(self, n, k):
        self.stack_array = [None]*n
        self.refrence_array = [None]*(n+k)
        self.last_index_array = [None]*k
        self.empty_index_list = [i for i in range(0, n)]
    # 
    def push(self, x, i):
        empty_index = self.empty_index_list.pop(0)
        self.stack_array[empty_index] = x
        self.refrence_array[empty_index] = self.last_index_array[i]
        self.last_index_array[i] = empty_index
        return True
    # 
    def pop(self, i):
        if self.last_index_array[i] is None:
            return None
        # 
        pop_element = self.stack_array[]
        temp_index = self.last_index_array[i]
        temp_item = self.refrence_array[temp_index]
        self.refrence_array[temp_index] = None
        self.last_index_array[i] = temp_item
        self.empty_index_list.append(temp_index)
        return pop_element

# -------------------------------------------------------------------------------------------------

arrangements = []

def towerOfHanoi(self, n, fromm, to, aux):
    """
    """
    towers = ''
    for i in range(1, n+1):
        towers = towers + str(i)
    # 
    self.result = '|'+'|' + towers
    towers = towers + '|'+'|'
    arrangements.append(towers)
    recursionTowerOfHanoi(towers, move)

merged_string = string1 + delimiter + string2 + delimiter + string3
demerged_list = merged_string.split(delimiter)

def recursionTowerOfHanoi(towers, move):
    """
    """
    if tower == self.result:
        return move
    # 
    tower_list = towers.split('|')
    # 
    # Tower 0 Move
    if len(tower_list[0]) > 0:
        if tower_list[0][0] < 

















# gas = [3, 7, 5, 2, 6, 16, 5, 5, 38, 4, 4, 9, 7, 4, 3, 5, 7]
# cost = [6, 5, 9, 3, 14, 9, 13, 3, 1, 14, 11, 8, 10, 7, 4, 4, 9]




# print(startStation(gas, cost))
