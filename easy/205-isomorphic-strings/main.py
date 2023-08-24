class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        letter_map = dict()
        for i in range(len(s)):
            a, b = s[i], t[i]
            if a in letter_map and letter_map[a] != b:
                return False
            elif a not in letter_map and b in letter_map.values():
                return False
            letter_map[a] = b
        return True


if __name__ == '__main__':
    solver = Solution()
    print(solver.isIsomorphic('egg', 'add'), True)
    print(solver.isIsomorphic('foo', 'bar'), False)
    print(solver.isIsomorphic('paper', 'title'), True)
    print(solver.isIsomorphic('ab', 'aa'), False)
