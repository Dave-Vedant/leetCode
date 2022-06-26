"""
Given the root of a binary tree and an integer targetSum, 
return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
"""

def hasPathSum(root,Targetsum):

    def dfs(node, curSum):
        if not node:
            return False
        
        curSum  += node.val
        if not node.left and not node.right:
            return curSum == Targetsum
        
        return dfs(node.left,curSum) or dfs(node.right, curSum)
    
    return dfs(root,0)

    # time complexity = O(N), space complexity = O(N) / or balanced tree O(logN)


    


    