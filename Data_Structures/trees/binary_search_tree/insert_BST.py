from inspect import currentframe

# time compelxity = O(H)/O(N) or O(log(N))
class BST:
    def __init__(self, val = 0 , left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def insertBST(root,value):

        current_node = root

        while current_node is not None:
            if value <= current_node.val:
                if current_node.left is None:
                    current_node.left = BST(value)
                    return root
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = BST(value)
                    return root
                else:
                    current_node = current_node.right
        return BST(value)

        # space : O(1)


# recursive...
    def insertBSTr(self, root, value):
        if not root:
            return BST(value)

        if value> root.val:
            root.right  = self.insertBSTr(root.right,value)
        else:
            root.left = self.insertBSTr(root.left, value)
        return root

        # space : O(logN) or O(H)/O(N) 