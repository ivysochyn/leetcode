class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        answ = 0
        for i in range(len(columnTitle)):
            answ += 26 ** i * (ord(columnTitle[-1-i]) - 64)
        return answ


if __name__ == "__main__":
    solver = Solution()
    print(solver.titleToNumber('A'), 1)
    print(solver.titleToNumber('AB'), 28)
    print(solver.titleToNumber('ZY'), 701)
