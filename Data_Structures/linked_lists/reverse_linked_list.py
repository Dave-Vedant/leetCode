"""Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]


Input: head = [1,2]
Output: [2,1]

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

"""

# two pointer

def reverseList(self, head):
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

    # time complexity = O(n), space complexity = O(1)

# original/ new head node
def reserveList1(head):
    if head is None:
        return head     # return None
    
    curr = head
    while head.next is not None:
        temp = head.next
        head.next = temp.next
        temp.next = curr
        
        curr = temp
    return curr


