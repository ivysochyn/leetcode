class Solution:
    def addBinary(self, a: str, b: str) -> str:
        answ = ""
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            answ += str(carry % 2)
            carry //= 2
        return answ[::-1]


if __name__ == "__main__":
    solver = Solution()
    print(solver.addBinary("11", "1"), "100")
    print(solver.addBinary("1010", "1011"), "10101")
    print(solver.addBinary("0", "0"), "0")
    print(solver.addBinary("0", "1"), "1")
