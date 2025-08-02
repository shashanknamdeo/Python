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


# def hasCycle(self, head):
#     """
#     """
#     slow = head
#     fast = head
#     while fast :
#         slow = slow.next
#         fast = fast.next
#         if fast == None:
#             return False
#         fast = fast.next
#         if slow == fast:
#             return True


# def mergeTwoLists(self, head1, head2):
#     dummy = ListNode(0)  # dummy head
#     current = dummy
#     # 
#     while head1 and head2:
#         if head1.val <= head2.val:
#             current.next = head1
#             head1 = head1.next
#         else:
#             current.next = head2
#             head2 = head2.next
#         current = current.next
#     # 
#     # One of head1 or head2 is not None
#     if head1:
#         current.next = head1
#     else:
#         current.next = head2
#     # 
#     return dummy.next  # skip dummy head


# def mergeTwoLists(self, head1, head2):
#     """
#     using resursive methoed
#     """
#     if not head1:
#         return head2
#     # 
#     if not head2:
#         return head1
#     # 
#     if head1.val < head2.val:
#         head1.next = self.mergeTwoLists(head1.next, head2)
#         return head1
#     # 
#     else:
#         head2.next = self.mergeTwoLists(head1, head2.next)
#         return head2


# def deleteNode(delNode):
#     """
#     """
#     if delNode and delNode.next:
#         next_node = delNode.next
#         delNode.val = next_node.val
#         delNode.next = next_node.next
#     # 
#     else:
#         return None


# def remove_duplicates(head):
#     """
#     """
#     current = head
#     last = None
#     unique_set = set()
#     # 
#     while current:
#         if current is in unique_set:
#             last.next = current.next
#             current =  current.next
#         # 
#         else:
#             unique_set.add(current.val)
#             last = current
#             current =  current.next
#     # 
#     return head


# def sort_list(head):
#     current = head

#     dummy_0 = ListNode(0)
#     dummy_1 = ListNode(0)
#     dummy_2 = ListNode(0)
#     # 
#     pointer_0 = dummy_0
#     pointer_1 = dummy_1
#     pointer_2 = dummy_2
#     # 
#     # Partition into three lists
#     while current:
#         val = current.val
#         if val == 0:
#             pointer_0.next = current
#             pointer_0 = pointer_0.next
#         elif val == 1:
#             pointer_1.next = current
#             pointer_1 = pointer_1.next
#         elif val == 2:
#             pointer_2.next = current
#             pointer_2 = pointer_2.next
#         current = current.next
#     # 
#     # Connect the lists: 0s -> 1s -> 2s
#     pointer_2.next = None  # end of list
#     pointer_1.next = dummy_2.next
#     pointer_0.next = dummy_1.next
#     # 
#     return dummy_0.next


# def multiplyLists(head1, head2):
#     temp1 = ""
#     temp2 = ""
#     # 
#     # Traverse first list
#     while head1:
#         temp1 += str(head1.val)
#         head1 = head1.next
#     # 
#     # Traverse second list
#     while head2:
#         temp2 += str(head2.val)
#         head2 = head2.next
#     # 
#     # Convert to integers
#     num1 = int(temp1)
#     num2 = int(temp2)
#     # 
#     # Multiply
#     result = num1 * num2
#     # 
#     # Convert result to linked list
#     dummy = ListNode(0)
#     current = dummy
#     for digit in str(result):
#         current.next = ListNode(int(digit))
#         current = current.next
#     # 
#     return dummy.next


# def removeNthFromEnd(self, head, n):
#     """
#     """
#     total_number = 0
#     current = head
#     while current:
#         current = current.next
#         total_number += 1
#     # 
#     target_node = total_number - n
#     current = head
#     node_number = 0
#     while node_number < target_node -1:
#         current = current.next
#         node_number += 1
#     # 
#     # print(target_node)
#     if target_node == 0:
#         return head.next
#     # 
#     next_node_1 = current.next
#     current.next = next_node_1.next
#     # 
#     return head


# def reorderList(self, head):
#         """
#         """
#         fast = head
#         slow = head
#         # 
#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next
#         # 
#         # print(slow.val)
#         head2 = reverseList(slow.next)
#         slow.next = None
#         # print(head2)
#         # 
#         current = head
#         while head2:
#             # print(head2.val)
#             current_next = current.next
#             head2_next = head2.next
#             current.next = head2
#             head2.next = current_next
#             current = current_next
#             head2 = head2_next
#         # 
#         return head


# def removeCycle(self, head):
#     slow = fast = head

#     # Step 1: Detect the loop
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#         if slow == fast:
#             break
#     else:
#         return head  # No loop found

#     # Step 2: Find the start of the loop
#     pointer_1 = head
#     pointer_2 = slow
#     if pointer_1 == pointer_2:
#         # Special case: cycle starts at head
#         while pointer_2.next != pointer_1:
#             pointer_2 = pointer_2.next
#     else:
#         while pointer_1.next != pointer_2.next:
#             pointer_1 = pointer_1.next
#             pointer_2 = pointer_2.next

#     # Step 3: Break the loop
#     pointer_2.next = None
#     return head


# def intersectPoint(head1, head2):
#     """
#     4 Approches
#     [Naive Approach]        Using two nested loops
#     [Better Approach]       Using Hashing 
#     [Expected Approach - 1] Using difference in node counts
#     [Expected Approach - 2] Using Two Pointer Technique
#     # 
#     solve using 4th Approch - Using Two Pointer Technique
#     Idea:
#         start pointer from both head
#         when pointer reach end restart this pointer from start of another list
#         same with 2nd pointer
#         where both poiter meet it is intersection
#     """
#     pointer_1 = head1
#     pointer_2 = head2
#     # 
#     while pointer_1 != pointer_2:
#         pointer_1 = pointer_1.next if pointer_1 else head2
#         pointer_2 = pointer_2.next if pointer_2 else head1
#     # 
#     return pointer_1  # or pointer_2 (both are same)


# def flatten_list(head):
# class ListNode:
#     def __init__(self, val, next=None, child=None):
#         self.val = val
#         self.next = next
#         self.child = child

# def flatten_list(head):
#     if not head:
#         return None
#     # 
#     current = head
#     child_head = ListNode(0)     # Dummy node to collect children
#     child_tail = child_head      # Tail pointer for child list
# # 
#     while current:
#         if current.child:
#             # Append current child list to tail
#             child_tail.next = current.child
#             # 
#             # Move tail to the end of newly added child list
#             temp = current.child
#             while temp.next:
#                 temp = temp.next
#             child_tail = temp
#             # 
#             current.child = None  # Optional: avoid dangling child pointers
#             # 
#         if current.next is None and child_head.next:
#             # Attach collected children to the end of this level
#             current.next = child_head.next
#             # 
#             # Reset dummy list for next level
#             child_head = ListNode(0)
#             child_tail = child_head
#         # 
#         current = current.next
#     # 
#     return head


# def zigZagList(head):
#     """
#     True : <
#     False : >
#     """
#     if not head or not head.next:
#         return head
#     # 
#     dummy = ListNode(0)
#     dummy.next = head
#     prev = dummy
#     curr = head
#     flag = True  # True means "<" expected
#     # 
#     while curr and curr.next:
#         if (flag and curr.val > curr.next.val) or (not flag and curr.val < curr.next.val):
#             # Swap nodes curr and curr.next
#             temp = curr.next
#             curr.next = temp.next
#             temp.next = curr
#             prev.next = temp
#             # 
#             # After swapping, update pointers
#             prev = temp
#         else:
#             prev = curr
#             curr = curr.next
#             # 
#         flag = not flag
#         # 
#     return dummy.next


# def reverseDLL(self, head):
#     """
#     """
#     current = head
#     # 
#     last_item = None
#     next_item = current.next
#     while next_item:
#         current.next, current.prev, last_item = last_item, next_item, current
#         current = next_item
#         next_item = next_item.next
#     # 
#     current.next, current.prev = last_item, next_item
#     # 
#     return current


# def removeNodes(self, head):
#     """
#     """
#     head = reverseList(head=head)
#     # 
#     current = head
#     while current and current.next:
#         while current.next and current.val > current.next.val:
#             current.next = current.next.next
#         # 
#         current = current.next
#     # 
#     return reverseList(head=head)


# def oddEvenList(self, head):
#     """
#     """
#     head_odd = ListNode('temp')
#     current_odd = head_odd
#     head_even = ListNode('temp')
#     current_even = head_even
#     current = head
#     # 
#     while current:
#         next_item = current.next
#         print(current.val)
#         # 
#         if current.val%2 == 1:
#             current_odd.next = current
#             current_odd = current_odd.next
#         # 
#         if current.val%2 == 0:
#             current_even.next = current
#             current_even = current_even.next 
#         # 
#         current.next = None
#         current = next_item
#     # 
#     current_even.next = head_odd.next
#     return head_even.next


def nextLargerNodes(self, head):
        """
        solve similer question of Leatcode
        https://leetcode.com/problems/next-greater-node-in-linked-list/
        concept - use stack to store max element
        """
        head = reverseList(head)
        max_node = [0]
        current = head
        answer = []
        # 
        while current:
            if max_node[0] <= current.val:
                max_node = [current.val]
                answer.append(0)
            # 
            else:
                next_node = max_node.pop()
                while next_node <= current.val:
                    next_node = max_node.pop()
                # 
                answer.append(next_node)
                max_node.append(next_node)
                max_node.append(current.val)
            # 
            current = current.next
        # 
        return answer[::-1]


def rearrangeLinkedListInPlace():
    """
    done this before
    reorderList(self, head)
    """


def sort_bitonic_dll_your_idea(head):
    if not head or not head.next:
        return head
    # 
    # Step 1: Go to the end of the list
    tail = head
    while tail.next:
        tail = tail.next
    # 
    # Step 2: Two pointers — one at start, one at end
    left = head
    right = tail
    # 
    # Dummy node to form the new sorted list
    dummy = Node(0)
    curr = dummy
    # 
    # Step 3: Compare left and right, link smaller node
    while left != right and left.prev != right:
        if left.data <= right.data:
            curr.next = left
            left.prev = curr
            left = left.next
        else:
            curr.next = right
            right.prev = curr
            right = right.prev
        curr = curr.next
    # 
    # Add the last remaining node (if left == right)
    if left == right:
        curr.next = left
        left.prev = curr
        curr = curr.next
    # 
    # Set tail of final list
    curr.next = None
    # 
    # Return head of new sorted DLL
    sorted_head = dummy.next
    if sorted_head:
        sorted_head.prev = None
    return sorted_head


def mergeKLists(self, lists):
    """
    best way - use a min heap
    """
    k = len(lists)
    heads = lists[:]  # copy of list heads
    dummy = ListNode(0)
    curr = dummy
    # 
    while True:
        min_index = -1
        min_val = float('inf')
        # 
        # Find the index of the smallest current node
        for i in range(k):
            if heads[i] and heads[i].val < min_val:
                min_val = heads[i].val
                min_index = i
        # 
        # If all heads are None, break
        if min_index == -1:
            break
        # 
        # Append the smallest node to result
        curr.next = heads[min_index]
        curr = curr.next
        # 
        # Move pointer forward in the selected list
        heads[min_index] = heads[min_index].next
    # 
    return dummy.next


def addListUsingRecursion(num1, num2):
    """
    """
    tail_1 = reverseList(num1)
    tail_2 = reverseList(num2)
    # 


def addNumber(digit, digit_1, digit_2, carry):
    """
    0 case
    """
    if not carry and digit1 and digit2:
        return None
    # 
    carry = carry if carry else 0
    digit_1 = digit_1 if digit_1 else ListNode(0)
    digit_2 = digit_2 if digit_2 else ListNode(0)
    # 
    summation = digit_1.val + digit_2.val + carry
    # 
    if summation//10 == 0 :
        digit.next = summation
        digit = digit.next
        return addNumber(digit=digit.next, digit_1=digit1.next, digit_2=digit2.next, carry=None)
    else:
        digit = summation//10
        digit = digit.next
        return digit.next = addNumber(digit=digit.next, digit_1=digit1.next, digit_2=digit2.next, carry=summation%10)


























# use set when want to find unique element 
# and also searching is o(1) < binary searching