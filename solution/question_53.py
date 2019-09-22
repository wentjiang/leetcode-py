class Solution:
    def maxSubArray(self, nums):
        temp = nums[0]
        max_sum = temp
        n = len(nums)
        for i in range(1, n):
            if temp + nums[i] > nums[i]:
                max_sum = max(max_sum, temp + nums[i])
                temp = temp + nums[i]
            else:
                max_sum = max(max_sum, temp, temp + nums[i], nums[i])
                temp = nums[i]
        return max_sum
