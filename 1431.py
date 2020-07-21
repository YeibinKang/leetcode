class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        
        answer = []
        largest = max(candies)

        for nums in candies:
            if nums+extraCandies >= largest:
                answer.append(True)
            else:
                answer.append(False)

        return answer