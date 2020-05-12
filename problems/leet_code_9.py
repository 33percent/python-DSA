"""
Given an integer number n, return the difference 
between the product of its digits and the sum of its digits.
"""


class Solution(object):
    def subtractProductAndSum(self, n:int) -> any:
        """
        :type n: int
        :rtype: int
        """
        digits = self.get_digits(n)
        sum_of_dig = sum(digits)
        return self.product_of_list(digits) - sum_of_dig

    def get_digits(self,n:int) -> list:
        digits = []
        while n > 0:
            digit = n % 10
            digits.append(digit)
            n = n//10
        return digits
    def product_of_list(self,n:list) -> int:
        result = 1
        for val in n:
            result = result * val
        return result
s = Solution()
print(s.subtractProductAndSum(441))

val:int = 10
print(type(val))