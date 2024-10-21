class Solution:
    def myAtoi(self, s: str) -> int:
        digit_start = False

        digits = ""
        for char in s.strip():
            if char.isdigit():
                digit_start = True
                digits = digits + char
                continue

            if digit_start != True and (char == "+" or char == "-"):
                digits = digits + char
                continue

            break

        return self.__round_string_to_32_bit_range(digits)

    def __round_string_to_32_bit_range(self, s: str) -> int:
        INT_MIN = -(2**31)
        INT_MAX = 2**31 - 1

        try:
            n = int(s)
        except ValueError:
            return 0

        if n < INT_MIN:
            return INT_MIN
        elif n > INT_MAX:
            return INT_MAX
        else:
            return n
