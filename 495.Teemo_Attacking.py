# -*- coding: utf-8 -*-


class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        max_time = 20000000
        if not timeSeries or duration < 0:
            return 0

        total = 0
        series_len = len(timeSeries)
        timeSeries.append(max_time)
        for i in range(series_len):
            if timeSeries[i] + duration < timeSeries[i+1]:
                total += duration
            else:
                total += timeSeries[i + 1] - timeSeries[i]
        return total


s = Solution()
print s.findPoisonedDuration([1, 2], 2)
