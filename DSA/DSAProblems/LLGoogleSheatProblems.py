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
    """
    """
    slow = head
    fast = head
    while fast :
        slow = slow.next
        fast = fast.next
        if fast == None:
            return False
        fast = fast.next
        if slow == fast:
            return True


def mergeTwoLists(self, head1, head2):
    dummy = ListNode(0)  # dummy head
    current = dummy
    # 
    while head1 and head2:
        if head1.val <= head2.val:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next
    # 
    # One of head1 or head2 is not None
    if head1:
        current.next = head1
    else:
        current.next = head2
    # 
    return dummy.next  # skip dummy head


def mergeTwoLists(self, head1, head2):
    """
    using resursive methoed
    """
    if not head1:
        return head2
    # 
    if not head2:
        return head1
    # 
    if head1.val < head2.val:
        head1.next = self.mergeTwoLists(head1.next, head2)
        return head1
    # 
    else:
        head2.next = self.mergeTwoLists(head1, head2.next)
        return head2


def deleteNode(delNode):
    """
    """
    if delNode and delNode.next:
        next_node = delNode.next
        delNode.val = next_node.val
        delNode.next = next_node.next
    # 
    else:
        return None


def remove_duplicates(head):
    """
    """
    current = head
    last = None
    unique_set = set()
    # 
    while current:
        if current is in unique_set:
            last.next = current.next
            current =  current.next
        # 
        else:
            unique_set.add(current.val)
            last = current
            current =  current.next
    # 
    return head


def sort_list(head):
    current = head

    dummy_0 = ListNode(0)
    dummy_1 = ListNode(0)
    dummy_2 = ListNode(0)
    # 
    pointer_0 = dummy_0
    pointer_1 = dummy_1
    pointer_2 = dummy_2
    # 
    # Partition into three lists
    while current:
        val = current.val
        if val == 0:
            pointer_0.next = current
            pointer_0 = pointer_0.next
        elif val == 1:
            pointer_1.next = current
            pointer_1 = pointer_1.next
        elif val == 2:
            pointer_2.next = current
            pointer_2 = pointer_2.next
        current = current.next
    # 
    # Connect the lists: 0s -> 1s -> 2s
    pointer_2.next = None  # end of list
    pointer_1.next = dummy_2.next
    pointer_0.next = dummy_1.next
    # 
    return dummy_0.next


def multiplyLists(head1, head2):
    temp1 = ""
    temp2 = ""
    # 
    # Traverse first list
    while head1:
        temp1 += str(head1.val)
        head1 = head1.next
    # 
    # Traverse second list
    while head2:
        temp2 += str(head2.val)
        head2 = head2.next
    # 
    # Convert to integers
    num1 = int(temp1)
    num2 = int(temp2)
    # 
    # Multiply
    result = num1 * num2
    # 
    # Convert result to linked list
    dummy = ListNode(0)
    current = dummy
    for digit in str(result):
        current.next = ListNode(int(digit))
        current = current.next
    # 
    return dummy.next


def removeNthFromEnd(self, head, n):
    """
    """
    total_number = 0
    current = head
    while current:
        current = current.next
        total_number += 1
    # 
    target_node = total_number - n
    current = head
    node_number = 0
    while node_number < target_node -1:
        current = current.next
        node_number += 1
    # 
    # print(target_node)
    if target_node == 0:
        return head.next
    # 
    next_node_1 = current.next
    current.next = next_node_1.next
    # 
    return head


def reorderList(self, head):
        """
        """
        fast = head
        slow = head
        # 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # 
        # print(slow.val)
        head2 = reverseList(slow.next)
        slow.next = None
        # print(head2)
        # 
        current = head
        while head2:
            # print(head2.val)
            current_next = current.next
            head2_next = head2.next
            current.next = head2
            head2.next = current_next
            current = current_next
            head2 = head2_next
        # 
        return head


def removeCycle(self, head):
    slow = fast = head
    # 
    # Step 1: Detect the loop
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return head  # No loop found
    # 
    # Step 2: Find the start of the loop
    pointer_1 = head
    pointer_2 = slow
    if pointer_1 == pointer_2:
        # Special case: cycle starts at head
        while pointer_2.next != pointer_1:
            pointer_2 = pointer_2.next
    else:
        while pointer_1.next != pointer_2.next:
            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.next
    # 
    # Step 3: Break the loop
    pointer_2.next = None
    return head





















# use set when want to find unique element 
# and also searching is o(1) < binary searching