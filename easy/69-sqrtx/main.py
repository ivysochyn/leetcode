class Solution:
    def mySqrt(self, x: int) -> int:
        if (x <= 1):
            return x
        start, end = 1, x // 2
        while (start <= end):
            middle = start + (end - start) // 2
            answ = x // middle
            if middle < answ:
                start = middle + 1
            elif middle > answ:
                end = middle - 1
            else:
                return middle
        return end


if __name__ == "__main__":
    sol = Solution()
    print(sol.mySqrt(4), 2)
    print(sol.mySqrt(8), 2)
    print(sol.mySqrt(9), 3)
    print(sol.mySqrt(10), 3)
    print(sol.mySqrt(11), 3)
    print(sol.mySqrt(12), 3)
    print(sol.mySqrt(13), 3)
