"""You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []


"""
# python easy list solution...
def mergeTwoLists(list1, list2):
    for i in range(len(list2)):
        list1.append(list2[i])
    return sorted(list1)


list1 = []
list2 = [0]
print(mergeTwoLists(list1, list2))

# iteration...
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    preHead = ListNode(-1)
    prev = preHead

    while l1 and l2 is not None:
        if l1 <= l2:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next
    
    if l1 is not None:
        prev.next = l1
    else:
        prev.next =l2

    return preHead.next         #output the whole list...

    # time complexity = O(m+n), space complexity = O(1)

def mergeTwoLists(l1, l2):

    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val <= l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1                                     # return never come until, total loop complete .. its deep to deep loop...
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2
    # time complexity = O(m+n), space complexity = O(m+n)
    