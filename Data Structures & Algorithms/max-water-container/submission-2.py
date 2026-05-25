class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        res = 0
        while l<r:

            h = min(heights[l],heights[r])
            vol = h*(r-l)

            res = max(vol,res)

            if heights[r] >= heights[l]:
                l+=1
            else:
                r-=1
        return res