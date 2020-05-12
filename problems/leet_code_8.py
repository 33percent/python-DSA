"""
Given two arrays of integers nums and index. 
Your task is to create target array under the following rules:

Initially target array is empty.
From left to right read nums[i] and index[i], 
insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read 
in nums and index.
Return the target array.

It is guaranteed that the insertion operations will be valid.
"""


class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        # workflow
        # first create an empty list target
        # copy that list temporarily
        # loop through individual items index - i
        # split the list by i
        # insert at that position
        # add both the lists 
        # return the new one
        target = []
        for idx,val in enumerate(index):
            if not target:
                target.append(nums[idx])
            else:
                pr_list = target[:val]
                post_list = target[val:]
                new_list = pr_list +[nums[idx]] + post_list
                target = new_list
        return target

s = Solution()
print(s.createTargetArray([1,2,3,4,0],[0,1,2,3,0]))