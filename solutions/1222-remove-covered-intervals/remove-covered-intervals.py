# Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.
#
# The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.
#
# Return the number of remaining intervals.
#
#  
# Example 1:
#
#
# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
#
#
# Example 2:
#
#
# Input: intervals = [[1,4],[2,3]]
# Output: 1
#
#
#  
# Constraints:
#
#
# 	1 <= intervals.length <= 1000
# 	intervals[i].length == 2
# 	0 <= li < ri <= 105
# 	All the given intervals are unique.
#
#


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: x[0])
        preX, preY = intervals[0]
        ans = 1
        for x, y in intervals:
            if y <= preY:
                continue
            
            if x == preX:
                preY = y
                continue
            ans += 1
            preX = x
            preY = y
        return ans
        # O N*N
        # deleted = [0] * len(intervals)
        # for i in range(len(intervals)):
        #     x, y = intervals[i]
        #     if deleted[i] == 1:
        #         continue
        #     for j in range(len(intervals)):
        #         if deleted[j] == 1 or i == j:
        #             continue
        #         x1, y1 = intervals[j]
        #         if x <= x1 and y1 <=y:
        #             deleted[j] = 1
        # return len(list(filter(lambda x: not x, deleted)))
