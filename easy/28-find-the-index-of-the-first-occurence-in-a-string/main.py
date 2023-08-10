class Solution:
    def strStr(self, haystak: str, needle: str) -> int:
        if needle:
            needle_l = len(needle)
            first_char = needle[0]
            for i in range(len(haystak)):
                if (len(haystak[i:]) - needle_l < 0):
                    return -1
                elif (haystak[i] == first_char and
                      haystak[i:i+needle_l] == needle):
                    return i
            return -1
        return 0


if __name__ == "__main__":
    s = Solution()
    print(s.strStr("hello", "ll"), 2)
    print(s.strStr("aaaaa", "bba"), -1)
    print(s.strStr("", ""), -1)
    print(s.strStr("a", "a"), 0)
    print(s.strStr("mississippi", "issip"), 4)
    print(s.strStr("mississippi", "issipi"), -1)
    print(s.strStr("mississippi", "pi"), 9)
    print(s.strStr("mississippi", "issipi"), -1)
