class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Time = Average: O(log(N)), worst: O(N) --- space = O(1)
    def insert(self, value):
        currentNode = self

        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else: 
                    currentNode = currentNode.right
        return self

    def contains(self,value):
        currentNode = self

        if currentNode is not None:
            if value < currentNode.value:
                currentNode  = currentNode.left
            elif value> currentNode.value:
                currentNode = currentNode.right
            else:
                return True   # means value == currentNode
        return False
        
    def remove(self,value, parentNode = None):
        currentNode = self

        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:                            
                # we find the value
                if currentNode.left is not None and currentNode.right is not None:
                    # if both are not None then let's find the minimum value of right tree (most left of right tree)
                    currentNode.value = currentNode.right.getMinValue()
                    # remove the targeted value and set the (most left right) value as current Node
                    currentNode.right.remove(currentNode.value, currentNode)
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.left = currentNode.left.left
                        currentNode.right = currentNode.left.right
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.right = currentNode.right.right
                        currentNode.left = currentNode.right.left
                    else:
                        currentNode.value = None
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                break
        self

    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value




                
        







        