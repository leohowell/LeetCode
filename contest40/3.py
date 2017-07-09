# -*- coding: utf-8 -*-


class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        return self.foo(price, special, needs)

    @classmethod
    def foo(cls, price, special, needs):
        most = []
        for item in special:
            tmp = []
            for i in range(len(needs)):
                if item[i] != 0:
                    tmp.append(needs[i] // item[i])
            most.append(min(tmp))

        normal = sum([price[i] * needs[i] for i in range(len(needs))])

        if not most:
            return normal

        last = []
        for i, item in enumerate(most):
            for x in range(item):
                new_needs = []
                current = special[i][-1] * (x + 1)
                for index, item in enumerate(needs):
                    n = item - special[i][index] * (x + 1)
                    if n < 0:
                        continue
                    new_needs.append(n)
                if sum(new_needs) == 0:
                    last.append(current)
                else:
                    last.append(current + cls.foo(price, special, new_needs))
        if not last:
            return normal
        else:
            return min(min(last), normal)



print(Solution.foo([2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]))
print(Solution.foo([1,1,1],[[1,1,0,0],[2,2,1,9]],[1,1,0]))
print(Solution.foo([9,9],[[1,1,1]],[2,2]))
