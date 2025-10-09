from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        opening = ["(","{","["]
        closing = [")","}","]"]
        stack = deque()

        for i in s:
            
            if i in opening:
                stack.append(i)
            elif i in closing:
                if len(stack)!=0:
                    if stack[-1] == opening[closing.index(i)]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False