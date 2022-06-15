"""
Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]


Input: root = [2,1,1]
Output: [[1]]
"""
class TreeNode:
    def __init__(self, val =0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def findDuplicateSubtree(root):
        result = []
        hash = {}

        def dfs(node,path):
            if node:
                path += str(node.val)+ "-"+ dfs(node.left, path)+ "-" + dfs(node.right, path)

                if path in hash:
                    hash[path] += 1
                    if hash[path] == 1:
                        result.append(node)
                else:
                    hash[path] = 0

                return path
            else:
                return "#"      # to represent null node

        dfs(root, "")
        return result

# execution:
    
    
root =[2,2,2,3, None ,3, None]      # None for null
print(TreeNode.findDuplicateSubtree(root))                


                
                

