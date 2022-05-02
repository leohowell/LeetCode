# 91. 解码方法
# https://leetcode-cn.com/problems/decode-ways/


def solution(s: str) -> int:
    n = len(s)
    dp = [0] * n
    dp_1 = [0] * n
    dp_2 = [0] * n

    first = int(s[0])
    if first == 0:
        return 0
    elif first == 1:
        dp[0] = 1
        dp_1[0] = 1
    elif first == 2:
        dp[0] = 1
        dp_2[0] = 1
    else:
        dp[0] = 1

    for i in range(1, n):
        val = int(s[i])

        if val == 0:
            if dp_1[i-1] == 0 and dp_2[i-1] == 0:
                return 0
            else:
                dp[i] = dp_1[i-1] + dp_2[i-1]
        elif val == 1:
            dp_1[i] = dp[i-1]
            dp[i] = dp[i-1] + dp_1[i-1] + dp_2[i-1]
            dp_2[i] = 0
        elif val == 2:
            dp_2[i] = dp[i-1]
            dp[i] = dp[i - 1] + dp_1[i - 1] + dp_2[i - 1]
            dp_1[i] = 0
        elif val <= 6:
            dp[i] = dp[i - 1] + dp_1[i - 1] + dp_2[i - 1]
        else:
            dp[i] = dp[i-1] + dp_1[i-1]

    return dp[-1]


print(solution("11"))
print(solution("1111"))
print(solution("11111111"))
print(solution("1111111111111111"))
print(solution("1111111111111111111111111111"))
print(solution("111111111111111111111111111111111111111111111"))


# "12"
# "11106"
# "111"
# "1111"
# "11111"
# "111111"
# "1111111"
# "226"
# "12"
# "1010101010101010101010101010"
# "0"
# "11011011011011011110"
# "22022022022220"
# "2062268284768923756923479523749"
# "111111111111111111111111111111111111111111111"
