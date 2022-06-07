"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false


"""
def isValid(str):

    stack = []
    closeToOpen = {")": "(", "}": "{", "]": "["}  #hashing , if there is closing, means opeing is before that, otherwise its false. #Ex: "][" is False
    
    for char in str:
        if char in closeToOpen:                                # means the paratheses is closing
            if stack and stack[-1] == closeToOpen[char]:
                stack.pop()
            else:
                return False
        else:                                     # means the paranthese is opeing..
            stack.append(char)

    return True if not stack else False  # at the end each parantehese needs to be cancelout and return empty stack (not stack)

    # time complexity = O(n), space complexity = O(n)
    

    # faster solution
def isValid1(s):
    stack=[]
    mapping = {"}":"{",")":"(","]":"["}
    
    for char in s:
        if char in "([{":
            stack.append(char)
        else:
            top_element = stack.pop() if stack else "#"
        
        if mapping[char] != top_element:
            return False
    return len(stack) == 0 # empty...

