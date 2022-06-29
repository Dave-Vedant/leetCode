class BSTIterator:

    def __init__(self, root):
        self.node_sorted = []
        self.index = -1
        self.inOrder(root)

    def inOrder(self, root):
        if root is None:
            return
        
        self.inOrder(root.left)
        self.node_sorted.append(root.val)
        self.inOrder(root.right)

    def next(self):
        self.index += 1
        return self.node_sorted[self.index]

    def hasNext(self):
        return self.index +1 < len(self.node_sorted)


    # time complexity ::: next= O(1), hasNext = O(1)
    # space complexity ::: O(N)