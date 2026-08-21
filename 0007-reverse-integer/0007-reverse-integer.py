class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        result = 0

        while x != 0:
            digit = x % 10 if x > 0 else -(abs(x) % 10)
            x = (x - digit) // 10

            # Use fixed bounds because Python // floors negative numbers.
            if result > 214748364 or (
                result == 214748364 and digit > 7
            ):
                return 0

            if result < -214748364 or (
                result == -214748364 and digit < -8
            ):
                return 0

            result = result * 10 + digit

        return result