import time
start_time = time.time()

"""
problem statement:
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # brute force
        # loop through all the values and check if the balance is equal to the sum of current 
        # iteration and the balance
        result = []
        for idx1,init_val in enumerate(nums):
            updated_arr = nums[:idx1] + nums[idx1+1:]
            for indx2,val in enumerate(updated_arr):
                if (val + init_val) == target:
                    result.extend([idx1, indx2+1])
                    return result
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # create a hash table and loop through it every time to see if the balance is available in the hash table
        # example of two pass hashtable
        hash_t = {}
        for idx1, init_val in enumerate(nums):
            hash_t[idx1] = init_val
        for idx,val in enumerate(nums):
            balance = target - hash_t[idx]
            if balance in hash_t.values() and hash_t.keys()[hash_t.values().index(balance)] != idx:
                return [idx,hash_t.keys()[hash_t.values().index(balance)]]
    
    def twoSum2(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # create a hash table and look up in it every time instead of looping through again.
        # example of one pass hashtable
        hash_t = {}
        for idx1, init_val in enumerate(nums):
            balance = target - init_val
            if balance in hash_t:
                return [hash_t[balance],idx1]
            hash_t[init_val] = idx1
Ans = Solution()
print(Ans.twoSum(
    nums=[3,2,4,9], 
    target=6
    ))
print("--- %s seconds ---" % (time.time() - start_time))
print(Ans.twoSum1(
    nums=[3,2,4,9], 
    target=6
    ))
print("--- %s seconds ---" % (time.time() - start_time))
print(Ans.twoSum2(
    nums=[3,2,4,9], 
    target=6
    ))
print("--- %s seconds ---" % (time.time() - start_time))
