from solutions.q1_two_sum import Solution


# Example 1
def test_example1_solution_success():
    solution = Solution()
    output = solution.two_sum(
        nums=[2, 7, 11, 15],
        target=9,
    )

    assert output == [0, 1]


# Example 2
def test_example2_solution_success():
    solution = Solution()
    output = solution.two_sum(
        nums=[3, 2, 4],
        target=6,
    )

    assert output == [1, 2]


# Example 3
def test_example3_solution_success():
    solution = Solution()
    output = solution.two_sum(
        nums=[3, 3],
        target=6,
    )

    assert output == [0, 1]
