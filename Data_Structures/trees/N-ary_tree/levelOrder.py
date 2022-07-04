"""
Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]

"""

from threading import currentThread


def levleOrder(root):
    if root is None:
        return []
    
    output = []
    previous_layer = [root]

    while previous_layer:
        current_layer = []
        output.append([])

        for node in previous_layer:
            output[-1].append(node.val)
            current_layer.extend(node.children)
        previous_layer = current_layer
    
    return output
    # time complexity = O(N), space complexity = O(N)

