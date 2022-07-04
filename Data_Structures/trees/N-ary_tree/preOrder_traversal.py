from logging.config import valid_ident


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    # preOrder ===> Top-> Bottom and Left-> Right
    def preOrder(self, root):
        if root is None:
            return []

        stack = [root,]
        output = []

        while stack is not None:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])
        
        return output
        # time complexity = O(N), space complexity = O(N)
    
# execution...

