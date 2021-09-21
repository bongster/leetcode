# Given an integer array arr, return the length of a maximum size turbulent subarray of arr.
#
# A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.
#
# More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:
#
#
# 	For i <= k < j:
#
#
# 		arr[k] > arr[k + 1] when k is odd, and
# 		arr[k] < arr[k + 1] when k is even.
#
#
# 	Or, for i <= k < j:
#
# 		arr[k] > arr[k + 1] when k is even, and
# 		arr[k] < arr[k + 1] when k is odd.
#
#
#
#
#  
# Example 1:
#
#
# Input: arr = [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
#
#
# Example 2:
#
#
# Input: arr = [4,8,12,16]
# Output: 2
#
#
# Example 3:
#
#
# Input: arr = [100]
# Output: 1
#
#
#  
# Constraints:
#
#
# 	1 <= arr.length <= 4 * 104
# 	0 <= arr[i] <= 109
#
#


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        N = len(arr)
        if N == 1:
            return 1
        
        best = 1
        streak = 1
        previousSign = arr[1] - arr[0]
        for x, p in zip(arr, arr[1:]):
            if (x - p < 0 and previousSign > 0) or (x - p > 0 and previousSign < 0):
                streak += 1
            else:
                streak = 1
                if x != p:
                    streak = 2
            previousSign = x - p
            best = max(best, streak)
        return best
