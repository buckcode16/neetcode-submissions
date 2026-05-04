class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = []
        for c in s.lower():
            if c.isalnum():
                cleaned.append(c)
        
        cleaned = "".join(cleaned)
        rev = cleaned[::-1]

        return cleaned == rev
        

