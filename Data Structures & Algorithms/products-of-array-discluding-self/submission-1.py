class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_nums = len(nums)
        output = [1] * total_nums
        prefix = 1
        for x in range(total_nums):
            output[x] = prefix
            prefix *= nums[x]
        suffix = 1
        for i in range(total_nums-1,-1,-1):
            output[i] *= suffix
            suffix *= nums[i]
        return output

