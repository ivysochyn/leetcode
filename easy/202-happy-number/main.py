class Solution:
    def calcSquareSum(self, n: int) -> int:
        answer = 0
        while n:
            tmp = n % 10
            answer += tmp ** 2
            n //= 10
        return answer

    def isHappy(self, n: int) -> bool:
        fast = n
        while True:
            n = self.calcSquareSum(n)
            fast = self.calcSquareSum(fast)
            fast = self.calcSquareSum(fast)
            if fast == n:
                break
        return True if n == 1 else False


if __name__ == '__main__':
    solver = Solution()
    print(solver.isHappy(19), True)
    print(solver.isHappy(2), False)
    print(solver.isHappy(7), True)
    print(solver.isHappy(1111111), True)
