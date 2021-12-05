class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = [2,7,11,15]
        target = 9
        for i in range(len(nums)-1):
            if (nums[i] + nums[i+1] == target) :
                return i, i+1
        else : 
            return None
                  