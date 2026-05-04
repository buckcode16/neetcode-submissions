class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        res = []
        for s in strs:
            s_sort = "".join(sorted(s))

            if s_sort not in hm:
                hm[s_sort] = []    
            
            hm[s_sort].append(s)

        for k in hm:
            res.append(hm[k])

        return res