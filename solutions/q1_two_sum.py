from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)

        for i in range(0, length - 1):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []
