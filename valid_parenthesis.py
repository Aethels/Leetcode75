s = input("Enter parentheses: ") 

def isValid(s):
        stack = []
        hashmap = {"(": ")", "{": "}", "[": "]"}
        
        for char in s:
            if char in hashmap:
                stack.append(char) 
            elif not stack or hashmap[stack.pop()] != char :
                return False                  
            
        return True if not stack else False


if isValid(s):
    print("The string is well-formed.")
else:
    print("The string is not well-formed.")