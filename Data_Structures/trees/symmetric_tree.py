def isSymmetric(root):
    if not root:
        return  True
    
    def isMirror(t1, t2):
        if(t1 and t2):
            return (t1.val == t2.val) and isMirror(t1.left,t2.right) and isMirror(t1.right, t2.left)
        
        return t1 == t2             # this is the return required because of return condition
 
    return isMirror(root.left, root.right)

    # time complexity = O(N), space complexity = O(N)