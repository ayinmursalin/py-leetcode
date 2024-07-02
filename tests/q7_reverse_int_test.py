from solutions.q7_reverse_int import Solution


# Example 1
def test_example1_solution_success():
    solution = Solution()
    output = solution.reverse(x=123)

    assert output == 321


# Example 2
def test_example2_solution_success():
    solution = Solution()
    output = solution.reverse(x=-123)

    assert output == -321


# Example 3
def test_example3_solution_success():
    solution = Solution()
    output = solution.reverse(x=120)

    assert output == 21
