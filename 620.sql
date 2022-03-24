-- 620. 有趣的电影
-- https://leetcode-cn.com/problems/not-boring-movies/

select id, movie, description, rating
from cinema
where description != "boring"
    and mod(id, 2) = 1
order by rating desc
