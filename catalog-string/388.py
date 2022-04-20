# 388. 文件的最长绝对路径
# https://leetcode-cn.com/problems/longest-absolute-file-path/

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        # 思考 利用栈全遍历即可
        stack = []

        max_len = 0
        for item in input.split("\n"):
            # print(item)
            tab_size = item.count("\t")
            is_own_dot = "." in item

            if is_own_dot and tab_size == 0:  # 根目录下的文件
                max_len = max(max_len, len(item))
                continue

            if is_own_dot and tab_size > 0:  # 子目录下的文件
                stack = stack[:tab_size]
                item = item.replace("\t", "")
                current = sum([len(item) for item in stack]) + len(stack) + len(item)
                # print("=====", "/".join(stack) + "/" +  item)
                max_len = max(max_len, current)
                continue

            if not is_own_dot and tab_size == 0:  # 根目录
                stack = [item]
                continue

            if not is_own_dot and tab_size > 0:  # 非根目录
                stack = stack[:tab_size]
                stack.append(item.replace("\t", ''))
                continue

        return max_len
