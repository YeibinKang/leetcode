class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        counter = 0
        jewels = set(J) 
        for stone in S:
            if stone in jewels:
                counter += 1
        return counter