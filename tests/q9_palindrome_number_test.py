from solutions.q9_palindrome_number import Solution

# Example 1
def test_example1_solution_success():
    solution = Solution()
    output = solution.isPalindrome(121)

    assert output == True

# Example 2
def test_example2_solution_success():
    solution = Solution()
    output = solution.isPalindrome(-121)

    assert output == False

# Example 3
def test_example3_solution_success():
    solution = Solution()
    output = solution.isPalindrome(10)

    assert output == False
