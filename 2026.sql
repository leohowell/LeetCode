-- 2026. 低质量的问题
-- https://leetcode-cn.com/problems/low-quality-problems/

select problem_id
from Problems
where cast(likes as float) / (likes + dislikes) < 0.6
order by problem_id
