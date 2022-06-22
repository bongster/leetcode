# There is a broken calculator that has the integer startValue on its display initially. In one operation, you can:
#
#
# 	multiply the number on display by 2, or
# 	subtract 1 from the number on display.
#
#
# Given two integers startValue and target, return the minimum number of operations needed to display target on the calculator.
#
#  
# Example 1:
#
#
# Input: startValue = 2, target = 3
# Output: 2
# Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.
#
#
# Example 2:
#
#
# Input: startValue = 5, target = 8
# Output: 2
# Explanation: Use decrement and then double {5 -> 4 -> 8}.
#
#
# Example 3:
#
#
# Input: startValue = 3, target = 10
# Output: 3
# Explanation: Use double, decrement and double {3 -> 6 -> 5 -> 10}.
#
#
#  
# Constraints:
#
#
# 	1 <= startValue, target <= 109
#
#


class Solution:

    def brokenCalc(self, X: int, Y: int) -> int:
        # I used bfs but can't solving problem only need a - operation
        queue = []
        queue.append((Y, 0))
        checked = []
        
        while len(queue):
            q, queue = queue[0], queue[1:]
            y, c = q
            if y == X:
                return c
            if y <= X:
                return (X - y) + c

            if y % 2 == 0:
                queue.append((y // 2, c + 1))
            else:
                queue.append((y + 1, c + 1))
        # cnt = 0
        # while Y != X:
        #     if X >= Y: # I missed this condition. !! 
        #         return (X - Y) + cnt
        #     if Y % 2 == 0:
        #         Y = Y // 2
        #     else:
        #         Y += 1
        #     cnt += 1
        # return cnt
