from typing import List


class Solution:
    def merge(self,
              nums1: List[int],
              m: int,
              nums2: List[int],
              n: int
              ) -> None:
        """
        Do not return anything, modify nums1 in place instead.
        """
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if (nums1[i] > nums2[j]):
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        if j >= 0:
            nums1[k-j:k] = nums2[:j]
        return


if __name__ == "__main__":
    solver = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solver.merge(nums1, m, nums2, n)
    print(f"nums1: {nums1} | Expected: [1, 2, 2, 3, 5, 6]")

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    solver.merge(nums1, m, nums2, n)
    print(f"nums1: {nums1} | Expected: [1]")

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    solver.merge(nums1, m, nums2, n)
    print(f"nums1: {nums1} | Expected: [1]")

    nums1 = [0, 0, 0]
    m = 0
    nums2 = [1, 2, 3]
    n = 3
    solver.merge(nums1, m, nums2, n)
    print(f"nums1: {nums1} | Expected: [1, 2, 3]")
