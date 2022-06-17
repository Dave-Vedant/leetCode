# recursive approach...

def inOrderTraversal(root):
    result = []
    def inorder(root):
        if not root:
            return
        inorder(root.left)
        inorder(root.right)
        result.append(root.val)
    inorder(root)
    return result