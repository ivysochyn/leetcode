class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        answer = ''
        while columnNumber > 0:
            columnNumber -= 1
            answer += chr(columnNumber % 26 + 65)
            columnNumber //= 26
        return answer[::-1]


if __name__ == '__main__':
    solver = Solution()
    print(solver.convertToTitle(1), 'A')
    print(solver.convertToTitle(28), 'AB')
    print(solver.convertToTitle(52), 'AZ')
    print(solver.convertToTitle(701), 'ZY')
    print(solver.convertToTitle(2147483647), 'FXSHRXW')
