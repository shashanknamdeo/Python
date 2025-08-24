

def implementTwoStacksinOneArray():
    """
    n = given length of array
    unable to use OPPs concept to implement
    https://www.geeksforgeeks.org/dsa/implement-two-stacks-in-an-array/
    """
    array = [None]*n
    pointer_1 = -1
    pointer_1 = len(array)
    def push1(value):
        """
        """
        if pointer_1 + 1 < pointer_2:
            array[pointer_1] = value
            pointer_1 += 1
        else:
            print("Stack-1-is-full")
    # 
    # 
    def push2(value):
        """
        """
        if pointer_2 - 1 > pointer_1:
            array[pointer_1] = value
            pointer_1 -= 1
        else:
            print("Stack-2-is-full")
    # 
    # 
    def pop1():
        """
        """
        if pointer_1 > -1:
            pointer_1 -= 1
            return interval_array[pointer_1 + 1]
        else:
            print("Stack-1-is-empty")
            return -1
    # 
    # 
    def pop2():
        """
        """
        if pointer_1 < len(array):
            pointer_1 += 1
            return interval_array[pointer_1 - 1]
        else:
            print("Stack-2-is-empty")
            return -1


def evaluationOfPostfixExpression(array):
    """
    """
    stack = []
    # 
    for item in array:
        if item.isdigit():
            stack.append(int(item))
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            # 
            if item == "+":
                stack.append(val2 + val1)
            elif item == "-":
                stack.append(val2 - val1)
            elif item == "*":
                stack.append(val2 * val1)
            elif item == "/":
                stack.append(val2 / val1)
        # 
    return stack.pop()


class MyStack(object):
    """
    """
    def __init__(self):
        print('__init__')
        self.queue_1 = []
        self.queue_2 = []
        self.front_queue = self.queue_1
        self.back_queue = self.queue_2
    # 
    def push(self, x):
        print('push')
        self.front_queue.append(x)
    # 
    def pop(self):
        print('pop')
        if not self.front_queue:
            return None
        # 
        while len(self.front_queue) > 1:
            self.back_queue.append(self.front_queue.pop(0))
        # 
        self.front_queue, self.back_queue = self.back_queue, self.front_queue
        return self.back_queue.pop(0)
    # 
    def top(self):
        print('top')
        if not self.front_queue:
            return None
        # 
        while len(self.front_queue) > 1:
            self.back_queue.append(self.front_queue.pop(0))
        # 
        self.front_queue, self.back_queue = self.back_queue, self.front_queue
        self.top_int = self.back_queue.pop(0)
        self.front_queue.append(self.top_int)
        print(self.front_queue, self.back_queue, self.top_int)
        return self.top_int
    # 
    def empty(self):
        print('empty')
        if not self.front_queue:
            return True
        else:
            return False


def reverseQueue(self, queue):
    """
    """
    stack = []
    while not queue.empty():
        stack.append(queue.get())
    # 
    for _ in range(len(stack)):
        queue.put(stack.pop())
    # 
    return queue


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
    # 
    def node(self, data):
        self.data = data
        self.next = None
        self.prev = None
    # 
    def insert_first(self,data):
        self.next_node = node(self.data)
        self.next_node.prev = self.head
        self.head.next = self.next_node
        self.head = self.next_node
    # 
    def insert_last(self,data):
        prev_node = node(data)
        prev_node.next = tail
        tail.prev = prev_node
        tail = prev_node
    # 
    def isEmpty(self):
    # 
    def size(self):


        
    def remove_first(self):

        
    def remove_last(self):

        
    def display(self):

            
class Stack:
    def __init__(self):

    
    def push(self,data):

    
    def pop(self):

        
    def size(self):

    
    def display(self):

        
class Queue:
    def __init__(self):

    
    def enqueue(self,data):

    
    def dequeue(self):

        
    def size(self):

        
    def display(self):









