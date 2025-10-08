class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]
        for i in range(1,len(nums)):
            temp = max(nums[i], nums[i]*curr_max, nums[i]*curr_min)
            curr_min = min(nums[i], nums[i]*curr_max, nums[i]*curr_min)
            curr_max = temp
            max_prod = max(curr_max, max_prod)
        return max_prod