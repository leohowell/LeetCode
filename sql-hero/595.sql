-- 595. 大的国家
-- https://leetcode-cn.com/problems/big-countries/

select name, population, area
from World
where area >= 3000000 or population >= 25000000
