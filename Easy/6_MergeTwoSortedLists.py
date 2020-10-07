"""
Merge two sorted linked lists and return it as a new sorted list. 
The new list should be made by splicing together the nodes of the first two
lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""


def mergeTwoLists(l1, l2):
    if not l1 and not l2:
        return l1

    if not l1:
        return l2
    if not l2:
        return l1

    result = ListNode()
    current = result

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1

            current = current.next
            l1 = l1.next
        else:
            current.next = l2

            current = current.next
            l2 = l2.next

    if l1:
        current.next = l1
    if l2:
        current.next = l2

    return result.next
    

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
