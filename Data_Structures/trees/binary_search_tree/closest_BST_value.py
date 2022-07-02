# main function
def findClosestValueInBST(root,target):
    return findClosestValue_i(root, target, float("inf"))


# recursive
def findClosestValue_r(root, target, closest):
    if root is None:
        return closest
    
    if abs(target - closest) > abs(target - root.value):
        closest = root.value
    
    if target < root.value:
        return findClosestValue_r(root.left, target, closest)
    elif target > root.value:
        return findClosestValue_r(root.right, target, closest)
    else:
        return closest



# interative
def findClosestValue_i(root, target, closest):
    currentNode = root
    while currentNode is not None:
        if abs(target-closest) > abs(target-currentNode.value):
            closest = currentNode.value
        
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break

    return closest


# NOTE:
# in both the cases space complexity = O(1)
# TIME COMPLEXITY : depends on tree type -- 
#               worst case : one side tree O(N)or O(D) because we goest up to depth of tree | 
#               for balanced tree: O(log(N)) ::: 









# iterative
