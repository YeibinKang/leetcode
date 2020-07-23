class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        product = 1
        sum = 0
        result = 0
        
        for i in str(n):
            product = product*int(i)
            sum = sum+int(i)
            
        result = product - sum
        return result
        
        
        
        