from solutions.q2_add_two_numbers import Solution


# Example 1
def test_example1_solution_success():
    solution = Solution()
    
    output = solution.add_two_numbers(
        l1=solution.list_to_listnode(values=[2, 4, 3]),
        l2=solution.list_to_listnode(values=[5, 6, 4]),
    )

    assert solution.listnode_to_list(head=output) == [7, 0, 8]


# Example 2
def test_example2_solution_success():
    solution = Solution()
    output = solution.add_two_numbers(
        l1=solution.list_to_listnode(values=[0]),
        l2=solution.list_to_listnode(values=[0]),
    )

    assert solution.listnode_to_list(head=output) == [0]


# Example 3
def test_example3_solution_success():
    solution = Solution()
    output = solution.add_two_numbers(
        l1=solution.list_to_listnode(values=[9, 9, 9, 9, 9, 9, 9]),
        l2=solution.list_to_listnode(values=[9, 9, 9, 9]),
    )

    assert solution.listnode_to_list(head=output) == [8, 9, 9, 9, 0, 0, 0, 1]
