class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''

        for s in strs:
            lenS = len(s)
            res+= str(lenS) + '#' + s
        return res
            

    def decode(self, s: str) -> List[str]:
        l = 0
        res = []

        while l < len(s):
            delim_idx = l
            while s[delim_idx] != '#':
                delim_idx+=1
            lenW = int(s[l:delim_idx])
            word = s[delim_idx+1:delim_idx+1+lenW]
            res.append(word)
            l = delim_idx + 1 + lenW
            
        return res


