class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        col_num = 0
        for char in columnTitle:
            col_num = col_num * 26 + (ord(char) - 64)
        return col_num


if __name__ == "__main__":
    solver = Solution()
    print(solver.titleToNumber('A'), 1)
    print(solver.titleToNumber('AB'), 28)
    print(solver.titleToNumber('ZY'), 701)
