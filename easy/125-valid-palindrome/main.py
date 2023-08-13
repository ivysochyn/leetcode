class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            elif not s[j].isalnum():
                j -= 1
                continue
            elif s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama"), True)
    print(solution.isPalindrome(""), True)
    print(solution.isPalindrome(" "), True)
    print(solution.isPalindrome("0P"), False)
    print(solution.isPalindrome("race a car"), False)
