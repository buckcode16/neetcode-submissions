class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def divide(arr):

            if len(arr) <= 1:
                return arr

            mid = len(arr)//2

            lh = arr[:mid]
            rh = arr[mid:]

            lh_num = divide(lh)
            rh_num = divide(rh)

            return merge(lh_num,rh_num)


        def merge(arr1,arr2):

            res = []
            i,j = 0,0

            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    res.append(arr1[i])
                    i+=1
                else:
                    res.append(arr2[j])
                    j+=1

            res.extend(arr1[i:])
            res.extend(arr2[j:])

            return res

        return divide(nums)