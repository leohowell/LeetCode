-- 178. 分数排名
-- https://leetcode-cn.com/problems/rank-scores/


select score,
       dense_rank() over (order by score desc) as "rank"
from Scores
