class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        while word1 and word2:
            merged += word1[0] + word2[0]
            word1 = word1[1:]
            word2 = word2[1:]
        return merged + word1 + word2


if __name__ == "__main__":
    s = Solution()
    print(s.mergeAlternately("abc", "pqr"), "apbqcr")
    print(s.mergeAlternately("ab", "pqrs"), "apbqrs")
    print(s.mergeAlternately("abcd", "pq"), "apbqcd")
    print(s.mergeAlternately("", "pqr"), "pqr")
    print(s.mergeAlternately("abc", ""), "abc")
    print(s.mergeAlternately("", ""), "")
