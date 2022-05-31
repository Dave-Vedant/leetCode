""""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
"""
# Approach 1: Hash Table
def linked_list_cycle(self, head):
    node_seen = set()
    while head is not None:
        if head in node_seen:
            return True                  # return head 
        node_seen.add(head)
        head = head.next
    return False

# space complexity = O(n), time complexity = o(n)


# Approach 2: Two Pointers
def linked_list_cycle(self, head):
    if head is None:
        return False
    slow = head
    fast = head.next

    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True
# Space complexity: O(1) , time complexity : O(n) or O(n+k) --  n withoutloop + k withinloop


class hare_tortoise:

    def intersect(self, head):
        tortoise = head
        hare = head
        while hare is not None and hare.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return tortoise
        return None

    def detectCycle(self, head):
        if head is None:
            return None

        intersect = intersect(head)
        if intersect is None:
            return None

        ptr1 = head
        ptr2 = intersect
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1

    # time complexity = O(n), space complexity = O(1)
