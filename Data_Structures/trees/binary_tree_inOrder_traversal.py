# recursive solution
def inOrderTraversal(root):
    result = []
    def inorder(root):
        if not root:
            return
        inorder(root.left)
        result.append(root.val)
        inorder(root.right)
    inorder(root)
    return result
    # time complexity = O(N), space complexity = O(N)




# iterative solution:  (stack) - logic is same as recursive, here we are generating the stack manualy.
def inOrderTraversal_stack(root):
    result = []
    stack = []
    cur = root
    while cur or stack:
        while cur:                # first go left-left-left
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()              # if end, then pop it out (last element)
        result.append(cur.value)       # add  pop element to result
        cur = cur.right                # Now check Right.
    return result





    return 
