"""
Given the head of a singly linked list, return true if it is a palindrome.

Input: head = [1,2,2,1]
Output: true

Input: head = [1,2]
Output: false

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
"""

# copy into aray list and two pointer technique...
def isPalindrome(self, head):
    vals = []
    while head is not None:
        vals.add(head)
        head = head.next
    
    if vals == vals[::-1]:
        return True
    return False
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# reverse second half in-place...

# helper function
def end_of_first_half(head):
    fast = head
    slow = head
    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow

def reverse_list(head):
    prev = None
    curr = head
    while curr is not None:
        temp = curr.next
        curr.next = temp.next
        prev = curr
        curr = temp
    return prev

# main
def isPalindrome(head):
    if head is None:
        return True

    first_half_end = end_of_first_half(head)
    second_half_start = reverse_list(head)

    result = True
    first_position = head
    second_position = second_half_start

    while result and second_position is not None:
        if first_position.val != second_position.val:
            result = False
        first_position = first_position.next
        second_position = second_position.next

    # restore the list and return the result
    first_half_end.next = reverse_list(second_half_start)
    return result

    # time complexity = O(n), space complexity = O(1)


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-

# Recursive function...
def isPalinderome(self, head):
    front_pointer = head

    def recursive_check(current_node = head):
        if current_node is not None:
            if not recursive_check(current_node.next):
                return False
            if front_pointer.val != current_node.val:
                return False
            front_pointer = front_pointer.next
        return True
    return recursive_check()
    
    # time complexity = O(n) , space complexity = O(n)


