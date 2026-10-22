class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for a in range(len(nums)):
            for i in range(a+1, len(nums)):
                if nums[a] == nums[i]:
                    return True
        return False
        