def inOrderSuccessor(root, p):
    successor = None

    while root is not None:

        if p.value >= root.value:
            root = p.right
        else:
            successor = root
            root = p.left

    return successor
    # time complexity = O(N) and for balanced tree O(log(N)), and space complexity = O(1)
