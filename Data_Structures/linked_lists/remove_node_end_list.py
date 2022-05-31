"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]v


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""
# two pointers

def removeNthFromEnd(head, n):
    slow = head
    fast = head

    for i in range(0, n):
        if fast.next is None:
            if i == n -1:
                head = head.next
            return head
        fast = fast.next
    
    while fast.next is not None:
        slow = slow.next
        fast = fast.next
    if slow.next is not None:
        slow.next = slow.next.next
    return head


head = [1,2,3,4,5]
n = 2
print(removeNthFromEnd(head,n))