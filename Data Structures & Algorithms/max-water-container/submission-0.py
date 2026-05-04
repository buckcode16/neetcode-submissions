class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l, r = 0, len(heights)-1
        highestVol = 0

        while l < r:
            currentVol = min(heights[l],heights[r])*(r-l)

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

            highestVol = max(highestVol, currentVol)
        return highestVol


