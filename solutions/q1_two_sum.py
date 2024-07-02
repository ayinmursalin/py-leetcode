class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        length = len(nums)

        for i in range(0, length - 1):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []
