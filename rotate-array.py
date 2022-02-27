from typing import List


# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         i = len(nums)-k%len(nums)
#         tmp = nums[i:]
#         tmp.reverse()
#         del nums[i:]
#         for n in tmp:
#             nums.insert(0,n)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        c = k%l
        for i in range(c):
            tmp = nums[-1]
            del nums[-1]
            nums.insert(0,tmp)




l = [1,2,3,4,5,6,7]
Solution().rotate(l,3)
print("outside",l)