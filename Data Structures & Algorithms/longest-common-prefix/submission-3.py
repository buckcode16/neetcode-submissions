class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 0:
            return ""

        sort = sorted(strs)

        i = 0
        res = ""
        first = sort[0]
        last = sort[-1]
        while i < len(first) and i < len(last):
            if first[i] == last[i]:
                res += first[i]
                i += 1
            else:
                break

        return res
