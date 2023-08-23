class Solution:
    def hammingWeight(self, n: int) -> int:
        if n > 0:
            counter = 0
            from math import log, ceil
            for i in range(ceil(log(n, 2)) + 1):
                counter += n % 2
                n >>= 1
            return counter
        return 0


if __name__ == '__main__':
    solver = Solution()
    print(solver.hammingWeight(0b00000000000000000000000000001011), 3)
    print(solver.hammingWeight(0b00000000000000000000000010000000), 1)
    print(solver.hammingWeight(0b11111111111111111111111111111101), 31)
    print(solver.hammingWeight(0b00000000000000000000000000000000), 0)
