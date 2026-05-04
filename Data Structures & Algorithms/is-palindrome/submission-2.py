import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.split()
        # s = "".join(s)

        s= re.sub(r'[^a-zA-Z0-9]','',s).lower()
        r = s[::-1]

        return s == r