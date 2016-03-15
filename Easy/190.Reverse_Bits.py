class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        bin_n = '%0.32d' % int(str(bin(n))[2:])
        return int(bin_n[::-1], base=2)
	
