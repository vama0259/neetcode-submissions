class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i, j in zip(range(len(nums)), nums):
            a[i] = j
        

        print(a)
        nums = sorted(nums)

        start = 0
        end = len(nums) - 1

        while start < end:
            sum_value = nums[start] + nums[end]
            print(sum_value)
            if sum_value > target:
                print("I came in 1")
                end -= 1
            elif sum_value < target:
                print("I came in 2")
                start += 1
            elif sum_value == target:
                key_s = [key for key, val in a.items() if val == nums[start]]
                print(key_s)
                key_e = [key for key, val in a.items() if val == nums[end]]
                print(key_s, key_e)
                if key_s == key_e:
                    return sorted(key_s[:2])
                else:
                    return sorted([key_s[0], key_e[0]])

        return []