class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack:
                    return False
                end = stack[-1]
                if char == ")" and end != "(":
                    return False
                elif char == "}" and end != "{":
                    return False
                elif char == "]" and end != "[":
                    return False
                else:
                    stack.pop()
        if not stack:
            return True
        return False