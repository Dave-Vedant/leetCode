"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3

"""
from turtle import left


def maxDepth(root):

    if not root:
        return 0                             # return 0 because the depth will be 0
    else:
        left_height = maxDepth(root.left)
        right_height = maxDepth(root.right)
        return max(left_height,right_height) + 1
    # time complexity = O(N), space complexity = O(log(N))


# iterative approach:

def maxDepth(root):
    stack = []
    if root:
        stack.append((1,root))
    
    depth = 0 
    while stack:
        current_depth, root = stack.pop()
        if root:
            depth = max(depth, current_depth)
            stack.append((current_depth+1, root.left))
            stack.append((current_depth+1, root.right))
    return depth

    # time complexity = O(N), space complexity = O(logN)