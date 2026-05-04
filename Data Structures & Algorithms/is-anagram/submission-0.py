class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S = {}
        T = {}

        for i in range(len(s)):
            S[s[i]] = S.get(s[i], 0) + 1
        for i in range(len(t)):
            T[t[i]] = T.get(t[i], 0) + 1
            
        if S == T:
            return True
        else :
            return False