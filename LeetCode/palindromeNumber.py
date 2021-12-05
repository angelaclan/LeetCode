class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        xx = str(x)
        if xx[0] == '-' :
            return False 
        if xx[::-1] == xx :
            return True
            