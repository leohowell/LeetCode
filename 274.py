from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # [3, 0, 6, 1, 5]
        # [6, 5, 3, 1, 0]
        citations = sorted(citations, reverse=True)
        if citations[0] < 1:
            return 0
        h_index = 1
        for item in citations[1:]:
            if item <= h_index:
                break
            h_index += 1

        return h_index
