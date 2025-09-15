
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


# # -------------------------------------------------------------------------------------------------


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

# s = ''
s = '()))((())()(('

print(maxLength(string=s))