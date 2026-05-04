class Solution:
    def isValid(self, s: str) -> bool:
        hm = {
            ')': '(','}':'{',']':'['
        }

        stack = []
        for b in s:
            if b in hm:
                if stack and stack[-1] == hm[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)

        return True if not stack else False