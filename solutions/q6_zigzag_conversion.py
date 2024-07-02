class Solution:
    def convert(self, s: str, numRows: int) -> str:
        length = len(s)
        stepper = 3 + (2 * (numRows - 3))
        indexes = []
        middle = stepper
        
        if stepper <= 0:
            return s

        for i in range(0, numRows):
            if i < length:
                indexes.append(i)
            
            if i != 0 and i < (numRows - 1):
                middle -= 2

            end = i
            while True:
                if i != 0 and i < (numRows - 1):
                    idx = end + middle + 1
                    if idx < length:
                        indexes.append(end + middle + 1)

                end += stepper + 1
                if end >= length:
                    break
                else:
                    indexes.append(end)

        return ''.join(list(map(lambda idx: s[idx], indexes)))
        