from solutions.q8_atoi import Solution

# Example 1
def test_example1_solution_success():
    solution = Solution()
    output = solution.myAtoi("42")

    assert output == 42

# Example 2
def test_example2_solution_success():
    solution = Solution()
    output = solution.myAtoi(" -042")

    assert output == -42

# Example 3
def test_example3_solution_success():
    solution = Solution()
    output = solution.myAtoi("1337c0d3")

    assert output == 1337

# Example 4
def test_example4_solution_success():
    solution = Solution()
    output = solution.myAtoi("0-1")

    assert output == 0

# Example 4
def test_example5_solution_success():
    solution = Solution()
    output = solution.myAtoi("words and 987")

    assert output == 0
