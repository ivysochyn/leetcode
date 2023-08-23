class Solution:
    def reverseBits(self, n: int) -> int:
        answer = 0
        for i in range(32):
            answer <<= 1
            answer += n % 2
            n >>= 1
        return answer


if __name__ == "__main__":
    n = 0b00000010100101000001111010011100
    print(Solution().reverseBits(n), 964176192)
    n = 0b11111111111111111111111111111101
    print(Solution().reverseBits(n), 3221225471)
