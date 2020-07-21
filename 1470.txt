class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
   
        nums1 = nums[0:n]
        nums2 = nums[n:]
        nums3 = []
        number = n


        for i in range(n):
            nums3.append(nums1[i])
            nums3.append(nums2[i])
        return nums3