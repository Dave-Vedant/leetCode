class MyHashSet:
    """
    Hash operations: add, remove, contains, _hash
    """
    def __init__(self):
        self.keyRange = 769
        self.bucketArray = [Bucket() for i in range(self.keyRange)]          # BUCKET function()

    def _hash(self, key):              # hash is index
        return key % self.keyRange

    def add(self, key):
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].insert(key)

    def remove(self, key):
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].delete(key)

    def contains(self, key):
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].exists(key)


class Bucket:
    """
    Bucket is supporting main hash function, add: insert, remove:delete, contains: exists
    
    """
    def __init__(self):
        self.tree = BSTree()                 # Bucket supports different data structures... BSTree, linked list etc... this solution has BSTree approach

    def insert(self,value):
        self.tree.root = self.tree.insertIntoBST(self.tree.root, value)

    def delete(self, value):
        self.tree.root = self.tree.deleteNode(self.tree.root, value)
    
    def exists(self, value):
        return (self.tree.searchBST(self.tree.root, value) is not None)


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class BSTree:
    """
    Tree has own features: insert into BST, successor, predecessor, delete Node... 
    
    """
    def __init__(self):
        self.root = None
    
    def searchBST(self, root, val):
        if root is None or val == root.val:
            return root
        
        return self.searchBST(root.left, val) if val < root.val else self.searchBST(root.right, val)


    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        
        if val>root.val:
            root.right = self.insertIntoBST(root.right,val)
        elif val == root.val:
            return root
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root


    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val


    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val


    def deleteNode(self, root, key):
        if not root:
            return None
        
        if key> root.val:
            root.right = self.deleteNode(root.right, key)
        elif key< root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not (root.left or root.right):
                root = None
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
        
        return root