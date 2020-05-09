"""
Implement function ToLowerCase() that has a string parameter str, 
and returns the same string in lowercase.
"""

class Solution(object):
    def toLowerCase(self, my_string):
        """
        :type str: str
        :rtype: str
        """
        updated_string = []
        for indi in my_string:
            ord_val = ord(indi)
            if ord_val >= 65 and ord_val <= 90:
                updated_string.append(chr(ord_val + 32))
            else:
                updated_string.append(indi)
        return ''.join(updated_string)
print(Solution.toLowerCase(None,"LovelY"))