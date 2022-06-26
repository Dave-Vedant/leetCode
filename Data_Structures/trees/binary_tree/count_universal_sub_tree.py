def count_universal(root):
    
    def helper(root):
        if root is None:
            return True

        left_count, is_left_universal = helper(root.left)
        right_count, is_right_universal = helper(root.right)
        is_universal = True

        if not is_left_universal or not is_right_universal:
            is_universal == False
        
        if root.left != None and root.left.value != root.value:
            is_universal= False
        
        if root.right != None and root.right.value != root.value:
            is_universal =  False
        
        if is_universal:
            return (left_count + right_count +1, True)
        else:
            return(left_count + right_count, False)

    total_count, is_universal = helper(root)   
    return total_count


    # time complexity = O(N), space complexity = O(H)
                                                                