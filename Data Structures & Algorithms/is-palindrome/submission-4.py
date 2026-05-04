class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''
        for c in s.lower():
            if c.isalnum():
                cleaned+=c
        

        return cleaned == cleaned[::-1]
        

