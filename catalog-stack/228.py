from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        output = []
        stack = []
        for n in nums:
            if not stack:
                stack.append(n)
                continue

            if stack[-1] + 1 == n:
                stack.append(n)
                continue

            output.append(self.handle_stack(stack))
            stack = [n]
        if stack:
            output.append(self.handle_stack(stack))
        return output

    def handle_stack(self, stack: List[int]) -> str:
        if len(stack) == 1:
            return f"{stack[0]}"
        else:
            return f"{stack[0]}->{stack[-1]}"
