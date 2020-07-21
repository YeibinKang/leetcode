class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        answer = []

        for i, number in enumerate(nums):
            
            if i == 0:
                number = nums[i]
                answer.append(number)
            else:
                number = nums[i]+answer[i-1] 
                answer.append(number)
    
                

        return answer