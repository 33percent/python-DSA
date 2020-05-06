"""
Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.

"""

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        response = []
        highest = candies[0]
        for i in range(1,len(candies)):
            if candies[i] > highest:
                highest = candies[i]
        for candy in candies:
            if (candy + extraCandies) >= highest:
                response.append(True)
            else:
                response.append(False)
        return response

S = Solution()
print(S.kidsWithCandies(
    candies=[2,3,5,1,3],
    extraCandies=3
))
print(S.kidsWithCandies(
    candies=[4,2,1,1,2],
    extraCandies=1
))

print(S.kidsWithCandies(
    candies=[12,1,12],
    extraCandies=10
))

print(S.kidsWithCandies(
    candies=[1,7,1,8,4,2,1,1],
    extraCandies=1
))
#[false,true,false,true,true,false,false,false]
#[false,true,false,true,false,false,false,false]
