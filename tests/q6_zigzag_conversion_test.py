from solutions.q6_zigzag_conversion import Solution


# Example 1
def test_example1_solution_success():
    solution = Solution()
    output = solution.convert(
        s="PAYPALISHIRING",
        numRows=3,
    )

    assert output == "PAHNAPLSIIGYIR"


# Example 2
def test_example2_solution_success():
    solution = Solution()
    output = solution.convert(
        s="PAYPALISHIRING",
        numRows=4,
    )

    assert output == "PINALSIGYAHRPI"


# Example 3
def test_example3_solution_success():
    solution = Solution()
    output = solution.convert(
        s="A",
        numRows=1,
    )

    assert output == "A"
