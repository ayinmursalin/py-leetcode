from solutions.q4_median_array import Solution


# Example 1
def test_example1_solution_success():
    solution = Solution()
    output = solution.findMedianSortedArrays(
        nums1=[1, 3],
        nums2=[2],
    )

    assert output == 2


# Example 2
def test_example2_solution_success():
    solution = Solution()
    output = solution.findMedianSortedArrays(
        nums1=[1, 2],
        nums2=[3, 4],
    )

    assert output == 2.5
