class ListNode:
    def __init__(self, val=0, next= None):
        self.val = val
        self.next = next

def removeElements(head, val):
    sentinel = ListNode(0)
    sentinel.next = head

    curr, prev = head, sentinel
    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            # increase by 1...
            prev = curr
        curr = curr.next
    return sentinel.next

    # time complexity = O(n), space complexity = O(1)
