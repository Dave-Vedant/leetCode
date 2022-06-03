class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
        

def flatten(head):
    if not head:
        return

    pseudoHead = Node(0, None, head, None)
    prev = pseudoHead

    stack = []
    stack.append(head)

    while stack:
        curr = stack.pop()

        prev.next = curr
        curr.prev = prev

        if curr.next:
            stack.append(curr.next)

        if curr.child:
            stack.append(curr.child)
            curr.child = None       # remove the chld pointer, because we will create the new prev <==> curr relationship
        
        prev = curr # update index

    pseudoHead.next.prev = None
    return pseudoHead.next

    # time complexity = O(n), space complexity = O(n)