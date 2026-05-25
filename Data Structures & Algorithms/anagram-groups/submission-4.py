class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hm = {}
        
        for s in strs:
            
            sorted_s = "".join(sorted(s))

            if sorted_s not in hm:
                hm[sorted_s] = []

            hm[sorted_s].append(s)


        return list(hm.values())
            

            