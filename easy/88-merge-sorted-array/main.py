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
        index = 0
        total_l = m + n
        while nums2:
            if nums1[index] > nums2[0]:
                nums1[index + 1:] = nums1[index:-1]
                nums1[index] = nums2.pop(0)
            elif nums1[index] == 0 and (len(nums2) == (total_l - index)):
                nums1[index:] = nums2[:]
                break
            index += 1
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
