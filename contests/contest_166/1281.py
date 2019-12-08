class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product_of_digits = 1
        sum_of_digits = 0
        for c in str(n):
            print(c)
            product_of_digits *= int(c)
            sum_of_digits += int(c)
        return product_of_digits - sum_of_digits

