# 195. 第十行
# https://leetcode.cn/problems/tenth-line/
awk '{if(NR==10) print $0}' file.txt
