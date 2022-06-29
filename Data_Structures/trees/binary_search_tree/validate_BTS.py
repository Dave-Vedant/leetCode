def validateBST(tree):
    return validateBSThelper(tree, float("-inf"), float("inf"))

def validateBSThelper(tree, minVal, maxVal):
    if tree is None:
        return True
    
    if tree.value < minVal and tree.value > maxVal:
        return False
    
    leftIsValid = validateBSThelper(tree.left, minVal, tree.value)
    rightIsValid = validateBSThelper(tree.right, tree.value, maxVal)

    return leftIsValid and rightIsValid



# iterative
def isValidBST(root):
    if not root:
        return True

    stack = [root, float("-inf"), float("inf")]
    while stack:
        root, lower, upper = stack.pop()
        if root is None:
            continue
        val = root.val
        if val <= lower or val >=upper:
            return False
        stack.append((root.right, val, upper))
        stack.append((root.left, lower, val))
    return True