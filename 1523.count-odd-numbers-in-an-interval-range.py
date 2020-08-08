class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """

        if low == high:
            return int(low % 2 != 0)

        if low % 2 == 0:
            low += 1
        if high % 2 == 0:
            high -= 1

        return (high - low) / 2 + 1
