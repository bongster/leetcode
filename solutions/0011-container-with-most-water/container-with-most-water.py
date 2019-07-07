# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.
#
#  
#
#
#
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49. 
#
#  
#
# Example:
#
#
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
#


class Solution:
    def maxArea(self, height: List[int]) -> int:
#         brute force
        # res = [0] * len(height)
        # for i in range(len(height)):
        #     for j in range(i + 1, len(height)):
        #         sub_height = min(height[i], height[j])
        #         # print(sub_height, i, j)
        #         res[i] = max(res[i], sub_height * (j - i))
        # return max(res)
#     Two pointer approach
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            max_area = max(max_area, min(height[r], height[l]) * (r - l))
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
        return max_area
