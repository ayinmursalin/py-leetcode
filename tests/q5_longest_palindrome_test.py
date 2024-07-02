from solutions.q5_longest_palindrome import Solution


# Example 1
def test_example1_solution_success():
    solution = Solution()
    output = solution.longestPalindrome(s="babad")

    assert output == "bab"


# Example 2
def test_example2_solution_success():
    solution = Solution()
    output = solution.longestPalindrome(s="cbbd")

    assert output == "bb"
