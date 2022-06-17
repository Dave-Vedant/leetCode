"""

# left to right , level by level

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]


"""

# recursive
def levelOrder_traversal(root):
    result = []
    if not root:
        return result

    def order(node,level):
        if len(result) == level:
            result.append([])                # this is because of format we need, each level requre the list

        result[level].append(node.val)

        if node.left:
            order(node.left,level+1)
        if node.right:
            order(node.right, level+1)

    order(root,0)
    return result

    # time complexity = O(N), space complexity = O(N)