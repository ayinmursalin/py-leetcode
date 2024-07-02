from solutions.q3_longest_substring import Solution


# Example 1
def test_example1_solution_success():
    solution = Solution()
    output = solution.lengthOfLongestSubstring(s="abcabcbb")

    assert output == 3


# Example 2
def test_example2_solution_success():
    solution = Solution()
    output = solution.lengthOfLongestSubstring(s="bbbbb")

    assert output == 1


# Example 3
def test_example3_solution_success():
    solution = Solution()
    output = solution.lengthOfLongestSubstring(s="pwwkew")

    assert output == 3
