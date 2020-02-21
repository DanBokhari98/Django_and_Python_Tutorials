#Given an integer array, find three numbers
#whose product is maximum and output the maximum product.
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums) - 1
        return max(nums[0]*nums[1]*nums[n], nums[n-2]*nums[n-1] * nums[n])
