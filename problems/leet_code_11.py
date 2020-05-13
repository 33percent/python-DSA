"""
Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing
 at most one digit (6 becomes 9, and 9 becomes 6).
"""

class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = self.get_digits(num)
        highest_val = int(''.join(digits))
        for val in range(len(digits)):
            curr = []
            for idx,n in enumerate(digits):
                if idx == val:
                    current = '9' if n == '6' else '6'
                    curr.append(current)
                else:
                    curr.append(n)
            __a = int(''.join(curr))
            if highest_val < __a:
                highest_val = __a
        return highest_val
    def get_digits(self, num):
        digits = []
        while num > 0:
            digit = num % 10
            digits.append(str(digit))
            num = num // 10
        return digits[::-1]
    
s = Solution().maximum69Number(12342)
print(s)
