"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:


Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. 
If you correctly return the intersected node, then your solution will be accepted.

Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]
"""
#  hash table

def getIntersectionNode(headA, headB):
    node_in_A = set()
    while headA is not None:
        node_in_A.add(headA)
        headA = headA.next

    while headB is not None:
        if headB in node_in_A:
            return headB
        headB = headB.next
    return None

    # time complexity = O(n + m), space complexity = O(n)/O(m) whichever list length is greater...

# two pointers

def getIntersectionNode1(headA, headB):
    ptA = headA
    ptB = headB

    while ptA != ptB:
        ptA = headB if ptA is None else ptA.next
        ptB = headA if ptB is None else ptB.next
    
    return ptA

    # time complexity = O(n+m), space complexity = O(1)


# brute force 
def getIntersectionNode2(headA, headB):
    while headA is not None:

        while headB is not None:

            if headA == headB:
                return headA
            headB = headB.next

        headA = headA.next

    return None

    # time complexity = O(n*m) ~= O(n^2), space complexity= O(1) ==> thats why bruteforce appraoch is not favoured as it time consuming (code runs for days)
















