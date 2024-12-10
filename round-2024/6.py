class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
        #
        # 比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
        #
        # P   A   H   N
        # A P L S I I G
        # Y   I   R
        # 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
        #
        # 请你实现这个将字符串进行指定行数变换的函数：
        #
        # string convert(string s, int numRows);

        # PAY P ALI S HIR I NG
        # P     A     H     N
        # 12345678901234567890
        # 1     7     3     9
        # PAHNAPLSIIGYIR

        # P     I    N
        # A   L S  I G
        # Y A   H R
        # P     I
        # 1 4 7 10
        # 0 3 6 9
        # 1 2

        if numRows == 1:
            return s

        values = []  # N * j
        column = 0
        row = []
        for i, char in enumerate(s):
            if column % (numRows - 1) == 0:
                row.append(char)
                if len(row) == numRows:
                    values.append(row)
                    row = []
                    column += 1
            else:
                index = numRows - (column % (numRows - 1)) - 1
                val = [None] * numRows
                val[index] = char
                values.append(val)
                column += 1

        if row:
            row += [None] * (numRows - len(row))
            values.append(row)

        output = []
        for j in range(numRows):
            for i in range(len(values)):
                char = values[i][j]
                if char:
                    output.append(char)
        return "".join(output)


if __name__ == "__main__":
    result = Solution().convert("PAYPALISHIRING", 3)
    print(result)
    result = Solution().convert("PAYPALISHIRING", 4)
    print(result)
