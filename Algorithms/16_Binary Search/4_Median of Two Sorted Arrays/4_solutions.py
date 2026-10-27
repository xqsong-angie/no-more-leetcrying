#20261022

#答案
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # 确保 nums1 是较短的那个数组，这样二分范围更小，复杂度为 O(log(min(m, n)))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        half_len = (m + n + 1) // 2
        
        while low <= high:
            i = (low + high) // 2
            j = half_len - i
            
            # A[i-1] 是 nums1 左边的最大值，A[i] 是 nums1 右边的最小值
            # B[j-1] 是 nums2 左边的最大值，B[j] 是 nums2 右边的最小值
            nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
            nums1_right_min = float('inf') if i == m else nums1[i]
            
            nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right_min = float('inf') if j == n else nums2[j]
            
            # 检查切口是否正确
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # 找到了正确的切法！根据总长度奇偶性计算中位数
                if (m + n) % 2 == 1:
                    return max(nums1_left_max, nums2_left_max)
                else:
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2
            elif nums1_left_max > nums2_right_min:
                # nums1 左边太大，说明 i 切得太靠右了，需要往左移
                high = i - 1
            else:
                # nums1 左边太小，说明 i 切得太靠左了，需要往右移
                low = i + 1