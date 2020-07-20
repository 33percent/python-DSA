"""
Given an array arr, replace every element in that array 
with the greatest element among the elements to its right, 
and replace the last element with -1.

After doing so, return the array.
"""

class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        print(arr)
s = Solution()
print(s.replaceElements([17,18,5,4,6,1]))