# search the value of the Binary tree and then return the whole subree uder that value



# recursive solution...
def searchBST(root, value):
    if root is None or value == root.val:
        return root
    elif value < root.val:
        return searchBST(root.left,value)
    else:
        return searchBST(root.right, value)

    # time complexity = O(N)/O(1), average case: O(logN) , space complexity = O(H)


# iterative:
def searchBSTi(root,value):
    while root is not None and root.val != value:
        root = root.left if value < root.val else root.right
    return root
    # time complexity ::: worst= O(N)/ O(H), balanced tree = O(log(N)) | space complexity = O(1)

