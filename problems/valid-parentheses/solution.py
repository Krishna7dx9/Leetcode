class Solution(object):
    def isValid(self, s):
        
        required = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []

        for ch in s:
            if ch not in required:     # if it is not in required key it means it is an opening bracket
                stack.append(ch) 
            else:                  # if ch is closing bracket
                if not stack:      # stack is empty
                    return False
                else:              # stack not empty, then check top of stack has reqired opening
                    if stack[-1] == required[ch]:
                        stack.pop()
                    else:
                        return False

        return not stack