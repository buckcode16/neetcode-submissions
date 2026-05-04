class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for s in strs:
            sortStr = "".join(sorted(s))
            # Incorrect implementation : if hashmap[sortStr].get() is None:
            if hashmap.get(sortStr) is None:
                hashmap[sortStr] = []
            hashmap[sortStr].append(s)

        main_list = []
        for sl in hashmap:
            main_list.append(hashmap[sl])
        
        return main_list

