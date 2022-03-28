# -*- coding: utf-8 -*-


class Solution(object):
    def maxProduct(self, nums):
        max_product = None
        sub_nums = []
        has_zero = False

        for n in nums:
            if n != 0:
                sub_nums.append(n)
            else:
                if n == 0:
                    has_zero = True
                if sub_nums:
                    result = self.max_product_non_zero(sub_nums)
                    sub_nums = []
                    if max_product is None:
                        max_product = result
                    elif result > max_product:
                        max_product = result
        if sub_nums:
            result = self.max_product_non_zero(sub_nums)
            if max_product is None:
                max_product = result
            elif result > max_product:
                max_product = result

        if has_zero:
            return max_product if max_product > 0 else 0
        return max_product

    def max_product_non_zero(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        negative number position matters
        zero number position massters
        [-----x------x----0----x------]
        """
        if len(nums) == 1:
            return nums[0]

        first_negative = None
        last_negative = None
        before_first_negative = 1
        after_last_negative = 1
        between_negative = 1
        negative_count = 0
        for n in nums:
            if n < 0:
                negative_count += 1
                if first_negative is None:
                    first_negative = n
                elif last_negative is None:
                    last_negative = n
                else:
                    between_negative *= after_last_negative * last_negative
                    after_last_negative = 1
                    last_negative = n
            else:
                if first_negative is None:
                    before_first_negative *= n
                elif last_negative is None:
                    between_negative *= n
                else:
                    after_last_negative *= n

        if negative_count == 0:
            return before_first_negative * between_negative * \
                   after_last_negative
        elif negative_count % 2 == 0:
            return before_first_negative * between_negative * \
                   after_last_negative * first_negative * last_negative
        elif negative_count == 1:
            if before_first_negative > between_negative:
                return before_first_negative
            else:
                return between_negative
        else:
            a = before_first_negative * first_negative * between_negative
            b = between_negative * last_negative * after_last_negative
            print a, b
            return a if a > b else b


s = Solution()
print(s.maxProduct([1,2,-1,-2,2,1,-2,1]))
