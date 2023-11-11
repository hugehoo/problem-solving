class Solution:
    def isValid(self, s: str) -> bool:
        open = ["[", "(", "{"]
        close = {']': '[', ')': '(', "}": "{"}
        open_stack = []
        
        for bracket in s:
            if bracket in open:
                open_stack.append(bracket)
            else:
                if not open_stack:
                    return False
                if open_stack[-1] == close[bracket]:
                    open_stack.pop()
                else:
                    return False
        
        return False if open_stack else True


s = Solution()
print(s.isValid(")"))
# print(s.isValid("()"))
# print(s.isValid("()[]{}"))
# print(s.isValid("(]"))
