class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        value = int(str(x).replace("-", "")[::-1])
        result = value * -1 if is_negative else value

        if result <= (-(2**31)) - 1 or result >= (2**31) + 1:
            return 0

        return result
