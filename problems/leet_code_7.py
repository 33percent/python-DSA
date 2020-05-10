"""
Given an array nums of integers, 
return how many of them contain an even number of digits.

"""

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for indi in nums:
            count_of_number = self.get_count(indi)
            if count_of_number % 2 == 0:
                count += 1
        return count
    def get_count(self, val):
        count = 0
        while val != 0:
            val //= 10
            count += 1
        return count

s = Solution()
print(s.findNumbers([121,345,2,6,7896]))