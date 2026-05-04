class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_hm, t_hm = {}, {}

        for c in s:
            if c in s_hm:
                s_hm[c] = s_hm.get(c,0)+1
            else:
                s_hm[c] = 1

        for c in t:
            if c in t_hm:
                t_hm[c] = t_hm.get(c,0)+1
            else:
                t_hm[c] = 1

        return s_hm == t_hm