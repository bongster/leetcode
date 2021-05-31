# On a broken calculator that has a number showing on its display, we can perform two operations:
#
#
# 	Double: Multiply the number on the display by 2, or;
# 	Decrement: Subtract 1 from the number on the display.
#
#
# Initially, the calculator is displaying the number x.
#
# Return the minimum number of operations needed to display the number y.
#
#  
#
# Example 1:
#
#
# Input: x = 2, y = 3
# Output: 2
# Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.
#
#
# Example 2:
#
#
# Input: x = 5, y = 8
# Output: 2
# Explanation: Use decrement and then double {5 -> 4 -> 8}.
#
#
# Example 3:
#
#
# Input: x = 3, y = 10
# Output: 3
# Explanation:  Use double, decrement and double {3 -> 6 -> 5 -> 10}.
#
#
# Example 4:
#
#
# Input: x = 1024, y = 1
# Output: 1023
# Explanation: Use decrement operations 1023 times.
#
#
#  
#
# Note:
#
#
# 	1 <= x <= 109
# 	1 <= y <= 109
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
