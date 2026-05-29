class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        hm = {}
        l= 0
        res = 0

        for r in range(len(fruits)):
            
            current_fruit = fruits[r]
            hm[current_fruit] = hm.get(current_fruit, 0) + 1

            while len(hm) > 2:
                left_fruit = fruits[l]
                hm[left_fruit] -= 1

                if hm[left_fruit] == 0:
                    del hm[left_fruit]
                
                l+=1
            
            res = max(res,r-l+1)

        return res