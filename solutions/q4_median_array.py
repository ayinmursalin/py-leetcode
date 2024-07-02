import statistics

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.sort()
        nums2.sort()
        
        return statistics.median(nums1 + nums2)
            
            