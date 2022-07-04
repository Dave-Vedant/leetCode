

class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

    # Top->Bottom, Left-> Rigth
    def postOrder(self, root):
        if root is None:
            return []

        stack = [root,]
        output = []
        while stack:                
            root = stack.pop()
            if root is not None:
                output.append(root.val)
            for c in root.children:
                stack.append(c)

        return output[::-1]


""""
ISSUE with "if stack is not None: " vs "if stack:"

There are many objects which are not None but for which bool(obj) is False: 
for instance, an empty list, an empty dict, an empty set, an empty string. . .

Use if obj is not None when you want to test if an object is not None. 
Use if obj only if you want to test for general "falseness" -- whose definition is object-dependent.

https://stackoverflow.com/questions/18583162/difference-between-if-obj-and-if-obj-is-not-none/18583185#18583185
"""