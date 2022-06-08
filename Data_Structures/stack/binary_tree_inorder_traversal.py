"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Input: root = [1,null,2,3]
Output: [1,3,2]

Input: root = [1,null,2,3]
Output: [1,3,2]

"""
# recursion 

def inorderTraversal_R(root):
    result = []

    def inOrder(root):
        if not root:
            return
        
        inOrder(root.left)
        result.append(root.val)
        inOrder(root.right)
    inOrder(root)
    return result

    # time complexity = O(N), space complexity = O(N)


# Itervative Solution (Binary Tree Inorder traversal Algorithm, using stack)

def inorderTraversal_I(root):
    result = []
    stack = []
    cur = root

    while cur or stack:              # when the current pointer OR stack is not null
        while cur:
            stack.append(cur)              # add the pointer to stack and go left, its loop so we will reach to extreame left-left-left in tree...
            cur = cur.left
        
        cur = stack.pop()             # then, for traversal pop the last value and add to result, and after that also think about the possible right tree, so leftUP - right - (choce(left,right))
        result.append(cur.val)
        cur = cur.right

    return result

    # time complexity = O(N), sapce complexity = O(N)

input = None
print(inorderTraversal_I(input))


