# -*- coding: utf-8 -*-


class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        return self.foo(equation)

    @staticmethod
    def foo(eq):
        left, right = eq.split('=')

        def build(exp):
            if exp[0] not in ('-', '+'):
                exp = '+' + exp

            reform = []
            sub = []
            for c in exp[::-1]:
                if c == '+' or c == '-':
                    if sub[-1] == 'x':
                        sub.append('1')
                    sub.append(c)
                    reform.append([sub[0], int(''.join(sub[1:-1][::-1])), sub[-1]])
                    sub = []
                elif c == 'x':
                    sub.append(c)
                else:
                    if None not in sub and 'x' not in ''.join(sub):
                        sub.append(None)
                    sub.append(c)
            return reform

        def cal(exp):
            cons = 0
            x_num = 0
            for item in exp:
                if item[0] == 'x':
                    if item[2] == '+':
                        x_num += item[1]
                    else:
                        x_num -= item[1]
                else:
                    if item[2] == '+':
                        cons += item[1]
                    else:
                        cons -= item[1]
            return x_num, cons

        left, right = build(left), build(right)
        left_x, left_num = cal(left)
        right_x, right_num = cal(right)
        cons = right_num - left_num
        x_num = left_x - right_x

        if not x_num and cons:
            return "No solution"
        elif not x_num and not cons:
            return "Infinite solutions"
        else:
            return 'x={}'.format(int(cons / x_num))




print(Solution.foo('x+5-3+x=6+x-2'))
print(Solution.foo('x=x'))
print(Solution.foo("2x=x"))
print(Solution.foo("2x+3x-6x=x+2"))
print(Solution.foo("x=x+2"))
print(Solution.foo("-200x=-10000001"))
print(Solution.foo("x=100"))

