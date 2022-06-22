# Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.
#
# Note that operands in the returned expressions should not contain leading zeros.
#
#  
# Example 1:
#
#
# Input: num = "123", target = 6
# Output: ["1*2*3","1+2+3"]
# Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.
#
#
# Example 2:
#
#
# Input: num = "232", target = 8
# Output: ["2*3+2","2+3*2"]
# Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.
#
#
# Example 3:
#
#
# Input: num = "3456237490", target = 9191
# Output: []
# Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.
#
#
#  
# Constraints:
#
#
# 	1 <= num.length <= 10
# 	num consists of only digits.
# 	-231 <= target <= 231 - 1
#
#


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        
        def bt(idx, curr, prev, total):
            nonlocal num, target
            if idx >= len(num):
                if total == target: res.append(curr)
                return
            acc = ""
            for i in range(idx, len(num)):
                acc += num[i]
                inacc = int(acc)
                if idx == 0:
                    bt(i+1, acc, inacc, inacc)
                else:
                    bt(i+1, curr+"+"+acc, inacc, total + inacc)
                    bt(i+1, curr+"-"+acc, -inacc, total - inacc)
                    bt(i+1, curr+"*"+acc, prev * inacc, total - prev + prev * inacc)
                if acc == "0": break
                
        bt(0, "", 0, 0)
        return res
