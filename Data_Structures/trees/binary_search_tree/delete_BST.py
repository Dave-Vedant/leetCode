class deleteBST:
    def __init__(self, val= 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def successor(root):
    root = root.right
    while root.left:
        root = root.left
    return root.val

def predessor(root):
    root = root.left
    while root.right:
        root = root.right
    return root.val

def deleteNode(root, key):
    if not root:
        return None
    
    if key > root.val:
        root.right = deleteNode(root.right, key)
    elif key < root.val:
        root.left = deleteNode(root.left, key)
    else:
        if not (root.left or root.right):
            root = None
        elif root.right:
            root.val = successor(root)
            root.right = deleteNode(root.right, root.val)
        else:
            root.val = predessor(root)
            root.left = deleteNode(root.left, root.val)
    return root
