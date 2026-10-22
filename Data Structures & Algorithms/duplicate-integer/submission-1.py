class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ''' Check if len is 0 then return False. Sort the array and then check it's neighbour if same return true. No sum method as we do not know if series is continous '''
        if len(nums) == 0:
            return False
        nums = sorted(nums)
        for a in range(len(nums)-1):
            if nums[a] == nums[a+1]:
                return True
        return False
        