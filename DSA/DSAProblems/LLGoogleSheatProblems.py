def reverseList(head):
    """
    Given the head of a singly linked list
    we see input as a list but when leetcode give input it is a head pointer
    """
    current = head
    last = None
    # 
    while current:
        next_node = current.next
        current.next = last
        last = current
        current = next_node
    # 
    return last


def hasCycle(self, head):
    current = head
    last = None
    # 
    while current:
        next_node = current.next
        print(current.val)
        current = next_node