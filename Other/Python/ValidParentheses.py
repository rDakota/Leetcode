class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        if s == '':
            return false
        
        for i in s:
            if stack: # if elements exist in the list
                # if current element and last element appended to the top(back)
                # are valid parenthesis pop the element
                if i == ')' and stack[-1] == "(":
                    stack.pop() 
                elif i==']' and stack[-1] == "[":
                    stack.pop()
                elif i=='}' and stack[-1] == "{":
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i) # append to the stack if empty
        return len(stack) == 0 # we want the list to be empty
