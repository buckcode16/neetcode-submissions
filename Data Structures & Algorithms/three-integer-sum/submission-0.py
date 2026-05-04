class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i,n in enumerate(nums):
            
            # sorted list, target is 0, if n > 0, threeSum > target
            if n > 0:
                break

            # check if i can be -1, prevent python wrap around index logic
            # if current number is same as previous number
            # do not iterate and skip, cause it will result in duplicates
            if i > 0 and n == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1


            while l<r:
                threeSum = n + nums[l]+nums[r]
                if threeSum > 0:
                    r-=1
                elif threeSum < 0:
                    l+=1
                else:
                    res.append([n,nums[l],nums[r]])

                    l+=1

                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                    

        return res