s = input("Enter phrase: ") 

def isPalindrome(s):
                
        s = s.lower()
        s = "".join(c for c in s if c.isalnum())
    
        i = 0
        j = len(s) - 1
        
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

result = isPalindrome(s)

if result:
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")