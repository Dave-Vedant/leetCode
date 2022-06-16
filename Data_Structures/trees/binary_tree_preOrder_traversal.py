class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preOrderTraversal(root):
        stack = [root,]
        output = []

        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)

        return output
        # time complexiyt = O(N), space complexity = O(N)

# recursive solution:

def preOrderTraversal(root):
    if root is None:
        return []
    return [root.val] + preOrderTraversal(root.left)  + preOrderTraversal(root.right)
    # time complexity = O(N), space complexity = O(N) 

# EASY METHOD...
def preOrderTraversal_nc(root):
    result  = []
    def inorder(root):
        if not root:
            return
        result.append(root.val)
        inorder(root.left)
        inorder(root.right)
    inorder(root)
    return result

# Morris Traversal:
def preOrderTraversal(self,root):

    node = root
    output = []

    while node:
        if not node.left:
            output.append(node.val)
            node = node.right
        else:
            predecessor = node.left

            while predecessor.right and predecessor.right is not node:
                predecessor  = predecessor.right
            
            if not predecessor.right:
                output.append(node.val)
                predecessor.right = node
                node = node.left
            else:
                predecessor.right = None
                node = node.right
        
    return output

# execution:

root = TreeNode([1, None ,2,3])
print(Solution.preOrderTraversal([1,2,3]))