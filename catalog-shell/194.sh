# 194. 转置文件
# https://leetcode.cn/problems/transpose-file/
# 高频

COLS=$(head -1 file.txt | wc -w)
for ((i=1;i<=COLS;i++)); do
  awk -v col="$i" '{print $col}' file.txt | xargs
done
