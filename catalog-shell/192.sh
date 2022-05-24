# 192. 统计词频
# https://leetcode.cn/problems/word-frequency/
cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -nr | awk '{print $2,$1}'
